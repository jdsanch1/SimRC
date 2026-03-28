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
| Enfoque | Optimización convexa (DCP) | Programación matemática general |
| Variables | Continuas | Continuas, enteras, binarias |
| Verificación | Automática (convexidad) | No verifica convexidad |
| Uso ideal | Portafolios, regresión | MILP, scheduling, dieta |

### Problema de portafolio con restricción de riesgo (CVXPY)

$$
\max_{\mathbf{w}} \quad \boldsymbol{\mu}^\top \mathbf{w} \qquad \text{s.a.} \quad \mathbf{w}^\top Q \mathbf{w} \leq \text{max\_risk}, \quad \sum w_i = 1, \quad w \geq 0
$$

### Problema de dieta (Pyomo — MILP)

$$
\min_{\mathbf{x}} \quad \mathbf{c}^\top \mathbf{x} \qquad \text{s.a.} \quad N^{\min} \leq A\mathbf{x} \leq N^{\max}, \quad \mathbf{x} \in \mathbb{Z}_{\geq 0}
$$

---

## Referencias bibliográficas

### Optimización convexa (Boyd & Vandenberghe, 2004)

- **§4.1 Formulación general** (pp. 127–130): Boyd presenta la forma canónica de un problema de optimización convexa. El portafolio con restricción de riesgo cuadrática es un caso particular (QCQP convexo).

- **§7.1 Estimación bajo incertidumbre** (pp. 351–355): La programación estocástica trata con parámetros inciertos. Boyd muestra cómo formular problemas robustos que funcionan bien bajo diferentes escenarios.
  - Optimización robusta: min_w max_Σ∈U w'Σw donde U es un conjunto de incertidumbre
  - Esto conecta con la covarianza robusta de la Clase 5

- **§6.5 Problemas multi-objetivo** (pp. 311–314): Cuando hay múltiples objetivos en conflicto (rendimiento vs. riesgo vs. liquidez), Boyd formaliza la **frontera de Pareto** y el método de ponderaciones para encontrar soluciones eficientes.

- **§4.1.3 Problemas enteros vs. convexos**: Boyd explica por qué los problemas con variables enteras (como el problema de dieta en Pyomo) NO son convexos y requieren algoritmos diferentes (branch-and-bound, branch-and-cut). Esto justifica usar Pyomo+GLPK en vez de CVXPY para el MILP.

### Otros textos

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — **Libro completo** relevante como referencia.
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
