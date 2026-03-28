# Clase 15 — Programación estocástica con Pyomo y CVXPY

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/15.%20Clase%2015/13Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F15.%20Clase%2015%2F13Class%20NB.ipynb)

---

## Objetivo

Combinar **CVXPY** (optimización convexa) y **Pyomo** (programación matemática general) para resolver problemas de optimización bajo incertidumbre: portafolios con restricciones de riesgo y problemas de planificación con variables enteras.

---

## Contenido teórico

### CVXPY vs. Pyomo

| Característica | CVXPY | Pyomo |
|---------------|-------|-------|
| Enfoque | Optimización convexa — DCP (Boyd & Vandenberghe, 2004, §4.1) | Programación matemática general |
| Variables | Continuas | Continuas, enteras, binarias |
| Verificación | Automática (convexidad) | No verifica convexidad (los problemas con variables enteras no son convexos; Boyd & Vandenberghe, 2004, §4.1.3) |
| Uso ideal | Portafolios, regresión | MILP, scheduling, dieta |

### Problema de portafolio con restricción de riesgo (CVXPY)

$$
\max_{\mathbf{w}} \quad \boldsymbol{\mu}^\top \mathbf{w} \qquad \text{s.a.} \quad \mathbf{w}^\top Q \mathbf{w} \leq \text{max\_risk}, \quad \sum w_i = 1, \quad w \geq 0
$$

Este es un QCQP convexo (Boyd & Vandenberghe, 2004, §4.6). La programación estocástica extiende estos problemas a escenarios con parámetros inciertos, formulando problemas robustos del tipo $\min_w \max_{\Sigma \in \mathcal{U}} \mathbf{w}^\top \Sigma \mathbf{w}$ (Boyd & Vandenberghe, 2004, §7.1). Cuando hay múltiples objetivos en conflicto (rendimiento vs. riesgo vs. liquidez), la **frontera de Pareto** y el método de ponderaciones (Boyd & Vandenberghe, 2004, §6.5) permiten encontrar soluciones eficientes.

### Problema de dieta (Pyomo — MILP)

$$
\min_{\mathbf{x}} \quad \mathbf{c}^\top \mathbf{x} \qquad \text{s.a.} \quad N^{\min} \leq A\mathbf{x} \leq N^{\max}, \quad \mathbf{x} \in \mathbb{Z}_{\geq 0}
$$

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §4.1 (formulación general), §4.6 (QCQP), §6.5 (multi-objetivo), §7.1 (estimación bajo incertidumbre).
- **Birge, J. R. & Louveaux, F.** (2011). *Introduction to Stochastic Programming* (2nd ed.). Springer.
- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

---

## Navegación del curso

← **Anterior**: Clase 14: Opciones barrera
→ **Fin del curso**

---

*Archivo de apoyo para la Clase 15 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
