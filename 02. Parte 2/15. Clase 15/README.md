# Clase 15 — Optimización convexa (CVXPY) y programación estocástica (Pyomo)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/15.%20Clase%2015/13Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F15.%20Clase%2015%2F13Class%20NB.ipynb)

---

## Objetivo

Combinar CVXPY (optimización convexa) y Pyomo (programación matemática general) para resolver problemas financieros y de planificación bajo incertidumbre. Esta clase es la síntesis final del curso.

---

## Contenido teórico

### CVXPY vs. Pyomo

| Característica | CVXPY | Pyomo |
|---------------|-------|-------|
| **Enfoque** | Optimización convexa (DCP) | Programación matemática general |
| **Variables** | Continuas | Continuas, enteras, binarias |
| **Verificación** | Automática (convexidad) | No verifica convexidad |
| **Complejidad** | Polinomial (punto interior, Boyd §11.1) | NP-hard para enteros (branch-and-bound) |
| **Uso ideal** | Portafolios, regresión, SVM | MILP, scheduling, dieta |

### Portafolio con restricción de riesgo (QCQP)

El problema de maximizar rendimiento sujeto a un riesgo máximo es un QCQP (Boyd §4.4.2):

$$
\max_{\mathbf{w}} \quad \boldsymbol{\mu}^\top \mathbf{w}
$$

sujeto a:

$$
\mathbf{w}^\top \Sigma \, \mathbf{w} \leq \sigma_{\max}^2, \qquad \sum_i w_i = 1, \qquad w_i \geq 0
$$

La restricción de riesgo define un **elipsoide** en el espacio de pesos — un conjunto convexo cuando Σ es PSD.

### Optimización robusta (SOCP)

Cuando los rendimientos esperados μ son inciertos y pueden variar dentro de un elipsoide de radio ρ centrado en la estimación:

$$
\boldsymbol{\mu} \in \mathcal{U} = \{\hat{\boldsymbol{\mu}} + \rho \, \mathbf{u} : \|\mathbf{u}\|_2 \leq 1\}
$$

el peor caso para el rendimiento es:

$$
\min_{\boldsymbol{\mu} \in \mathcal{U}} \boldsymbol{\mu}^\top \mathbf{w} = \hat{\boldsymbol{\mu}}^\top \mathbf{w} - \rho \|\mathbf{w}\|_2
$$

El problema robusto se convierte en un **SOCP** (Boyd §7.1):

$$
\max_{\mathbf{w}} \quad \hat{\boldsymbol{\mu}}^\top \mathbf{w} - \rho \|\mathbf{w}\|_2
$$

sujeto a:

$$
\sum_i w_i = 1, \qquad w_i \geq 0
$$

A medida que ρ crece, los pesos convergen al portafolio de mínima varianza — la incertidumbre fuerza la diversificación.

### Problema de dieta (MILP con Pyomo)

El problema clásico de dieta minimiza costo sujeto a requerimientos nutricionales:

$$
\min_{\mathbf{x}} \quad \mathbf{c}^\top \mathbf{x}
$$

sujeto a:

$$
\mathbf{N}^{\min} \leq A\mathbf{x} \leq \mathbf{N}^{\max}, \qquad \sum_i V_i x_i \leq V^{\max}, \qquad x_i \in \mathbb{Z}_{\geq 0}
$$

Las variables enteras hacen que el problema sea NP-hard (Boyd §4.1.3). CVXPY rechazaría este problema; Pyomo lo resuelve con branch-and-bound (GLPK).

### Convexo vs. entero: por qué importa la distinción

| Propiedad | Problema convexo | Problema entero |
|-----------|:---:|:---:|
| Mínimo local = global | **Sí** | No |
| Soluble en tiempo polinomial | **Sí** | No (NP-hard) |
| Dualidad fuerte | **Sí** (Slater) | No en general |
| CVXPY puede resolverlo | **Sí** | No |
| Pyomo puede resolverlo | Sí | **Sí** |

---

## Resumen del curso completo

### Mapa de herramientas por clase

| Problema | Herramienta | Clases | Tipo Boyd |
|----------|-------------|:------:|-----------|
| Frontera eficiente | CVXPY | 4, 11 | QP (§4.4) |
| Max Sharpe (Charnes-Cooper) | CVXPY | 4, 9, 10 | QP (§4.3.2) |
| Portafolio con riesgo | CVXPY | 15 | QCQP (§4.4.2) |
| Portafolio robusto | CVXPY | 15 | SOCP (§7.1) |
| Regularización L₂/L₁ | CVXPY | 12 | QP (§6.3) |
| Tracking error | CVXPY | 12 | SOCP (§4.3.1) |
| Opciones barrera | Monte Carlo | 14 | No convexo |
| Dieta (enteros) | Pyomo | 15 | MILP |

### Flujo completo

```
Datos (yfinance)
  → Rendimientos logarítmicos
    → Estimadores robustos (Huber μ, Ledoit-Wolf Σ)
      → Simulación Monte Carlo
      │   ├── Portafolios (Clase 9)
      │   ├── Valuación de opciones (Clase 8)
      │   └── Opciones barrera (Clase 14)
      │
      → Optimización convexa (CVXPY/DCP)
      │   ├── QP: frontera eficiente (Clase 4, 11)
      │   ├── QCQP: restricción de riesgo (Clase 15)
      │   ├── SOCP: tracking error, robusta, CML (Clase 10, 12, 15)
      │   └── Charnes-Cooper: max Sharpe (Clase 4, 9, 10)
      │
      → Programación entera (Pyomo)
          └── MILP: problema de dieta (Clase 15)
```

---

## Recursos adicionales

### Documentación

| Recurso | Descripción |
|---------|-------------|
| [CVXPY](https://www.cvxpy.org/) | Optimización convexa (DCP) |
| [Pyomo](https://www.pyomo.org/) | Programación matemática general |
| [Boyd cvxbook (PDF)](https://web.stanford.edu/~boyd/cvxbook/) | Libro completo gratuito |
| [GLPK](https://www.gnu.org/software/glpk/) | Solver para MILP |

### Conexión con todas las clases

| Clase | Tema | Conexión con Clase 15 |
|:-----:|------|----------------------|
| 1–2 | Datos, rendimientos, covarianza | Insumos para optimización |
| 3 | Opciones (payoff convexo) | Convexidad de max(S-K,0) (Boyd §3.2.3) |
| 4 | Sharpe, frontera eficiente | QP de Markowitz (Boyd §4.4) |
| 5 | Shrunk Covariance | Regularización (Boyd §6.3) |
| 6 | Huber | Penalización robusta (Boyd §6.1.2) |
| 7 | VaR/CVaR | SOCP para CVaR (Boyd §4.3.2) |
| 8 | Valuación MC opciones | Convergencia 1/√N |
| 9–11 | MC vs Markowitz | CVXPY > MC para óptimos exactos |
| 12 | Regularización L₁/L₂ | Estabilización de pesos (Boyd §6.3) |
| 13 | Portafolio con bono | CML como SOCP |
| 14 | Opciones barrera | Límite de convexidad (Boyd §3.2) |

---

## Referencias bibliográficas

### Textos principales

- **Birge, J. R. & Louveaux, F.** (2011). *Introduction to Stochastic Programming* (2nd ed.). Springer.
- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §4.1.3, §4.4.2, §4.6, §6.5, §7.1, §11.1.
- **Charnes, A. & Cooper, W. W.** (1962). Programming with linear fractional functionals. *Naval Research Logistics Quarterly*, 9(3–4), 181–186.
- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
- **Markowitz, H.** (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

---

## Navegación del curso

← **Anterior**: Clase 14: Opciones barrera
→ **Fin del curso**

---

*Archivo de apoyo para la Clase 15 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
