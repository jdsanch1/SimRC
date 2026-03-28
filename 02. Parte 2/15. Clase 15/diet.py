"""
diet.py — Problema de dieta como MILP (Mixed-Integer Linear Program).

Curso: Simulación de Riesgos y Coberturas (SimRC), Clase 15
Profesor: Juan Diego Sánchez Torres — MAF ITESO

Formulación matemática:
    minimizar   Σᵢ cᵢ · xᵢ                    (costo total)
    sujeto a    Nⱼᵐⁱⁿ ≤ Σᵢ aᵢⱼ · xᵢ ≤ Nⱼᵐᵃˣ  (requerimientos nutricionales)
                Σᵢ Vᵢ · xᵢ ≤ Vᵐᵃˣ             (volumen máximo)
                xᵢ ∈ ℤ≥₀                        (porciones enteras)

Este es un problema de programación lineal entera mixta (MILP).
No es convexo (por las variables enteras), por lo que se resuelve
con Pyomo + GLPK (branch-and-bound) en lugar de CVXPY.

Uso:
    pyomo solve --solver=glpk diet.py dietdata.dat

O desde Python:
    from pyomo.environ import *
    instance = model.create_instance('dietdata.dat')
    solver = SolverFactory('glpk')
    results = solver.solve(instance)

Referencias:
    - Dantzig, G. B. (1963). Linear Programming and Extensions.
      Princeton University Press. (Formulación original del problema de dieta)
    - Boyd, S. & Vandenberghe, L. (2004). Convex Optimization. §4.1.3
      (Por qué los problemas enteros son NP-hard y no se resuelven con CVXPY)
    - Pyomo documentation: https://www.pyomo.org/
"""

from pyomo.environ import *

infinity = float('inf')

# ---------------------------------------------------------------------------
# Modelo abstracto (los datos se cargan desde dietdata.dat)
# ---------------------------------------------------------------------------
model = AbstractModel(doc="Problema de dieta — minimizar costo nutricional")

# --- Conjuntos ---
model.F = Set(doc="Conjunto de alimentos disponibles")
model.N = Set(doc="Conjunto de nutrientes requeridos")

# --- Parámetros ---
model.c = Param(
    model.F, within=PositiveReals,
    doc="Costo por porción de cada alimento ($)"
)
model.a = Param(
    model.F, model.N, within=NonNegativeReals,
    doc="Contenido del nutriente j en una porción del alimento i"
)
model.Nmin = Param(
    model.N, within=NonNegativeReals, default=0.0,
    doc="Requerimiento mínimo de cada nutriente"
)
model.Nmax = Param(
    model.N, within=NonNegativeReals, default=infinity,
    doc="Límite máximo de cada nutriente"
)
model.V = Param(
    model.F, within=PositiveReals,
    doc="Volumen por porción de cada alimento (oz)"
)
model.Vmax = Param(
    within=PositiveReals,
    doc="Volumen máximo total de alimento permitido (oz)"
)

# --- Variable de decisión ---
model.x = Var(
    model.F, within=NonNegativeIntegers,
    doc="Número de porciones de cada alimento (entero ≥ 0)"
)


# --- Función objetivo: minimizar costo total ---
def cost_rule(model):
    """min Σᵢ cᵢ · xᵢ"""
    return sum(model.c[i] * model.x[i] for i in model.F)


model.cost = Objective(rule=cost_rule, doc="Costo total de la dieta ($)")


# --- Restricción: requerimientos nutricionales ---
def nutrient_rule(model, j):
    """Nⱼᵐⁱⁿ ≤ Σᵢ aᵢⱼ · xᵢ ≤ Nⱼᵐᵃˣ para cada nutriente j"""
    value = sum(model.a[i, j] * model.x[i] for i in model.F)
    return model.Nmin[j] <= value <= model.Nmax[j]


model.nutrient_limit = Constraint(
    model.N, rule=nutrient_rule,
    doc="Requerimientos nutricionales mínimos y máximos"
)


# --- Restricción: volumen máximo ---
def volume_rule(model):
    """Σᵢ Vᵢ · xᵢ ≤ Vᵐᵃˣ"""
    return sum(model.V[i] * model.x[i] for i in model.F) <= model.Vmax


model.volume = Constraint(
    rule=volume_rule,
    doc="Volumen total no excede el máximo permitido"
)
