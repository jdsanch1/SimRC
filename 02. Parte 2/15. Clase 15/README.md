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

Este es un QCQP convexo (Boyd & Vandenberghe, 2004, §4.6).

#### Optimización robusta bajo incertidumbre elipsoidal (Boyd & Vandenberghe, 2004, §7.1)

**Teorema.** Cuando la matriz de covarianza es incierta y pertenece a un **conjunto de incertidumbre elipsoidal** $\mathcal{U} = \{\Sigma_0 + \sum_{i=1}^{L} u_i \Sigma_i : \|\mathbf{u}\|_2 \leq 1\}$, el problema de peor caso:

$$
\min_{\mathbf{w}} \max_{\Sigma \in \mathcal{U}} \; \mathbf{w}^\top \Sigma \mathbf{w} \quad \text{s.a.} \quad \boldsymbol{\mu}^\top \mathbf{w} \geq \mu^*, \; \mathbf{1}^\top \mathbf{w} = 1, \; \mathbf{w} \geq 0
$$

se reformula como un **SOCP**:

$$
\min_{\mathbf{w}, t} \; t \quad \text{s.a.} \quad \mathbf{w}^\top \Sigma_0 \mathbf{w} + \left\| \begin{pmatrix} \mathbf{w}^\top \Sigma_1 \mathbf{w} \\ \vdots \\ \mathbf{w}^\top \Sigma_L \mathbf{w} \end{pmatrix} \right\|_2 \leq t, \quad \boldsymbol{\mu}^\top \mathbf{w} \geq \mu^*, \; \mathbf{1}^\top \mathbf{w} = 1, \; \mathbf{w} \geq 0
$$

*Bosquejo de prueba.* El maximo interno $\max_{\|\mathbf{u}\|_2 \leq 1} \mathbf{w}^\top (\Sigma_0 + \sum_i u_i \Sigma_i) \mathbf{w}$ se evalua por Cauchy-Schwarz: $\max_{\|\mathbf{u}\| \leq 1} \mathbf{a}^\top \mathbf{u} = \|\mathbf{a}\|_2$ donde $a_i = \mathbf{w}^\top \Sigma_i \mathbf{w}$. El resultado es $\mathbf{w}^\top \Sigma_0 \mathbf{w} + \|\mathbf{a}\|_2$, que es convexo en $\mathbf{w}$ (composicion de funciones convexas con norma, Boyd & Vandenberghe, 2004, §3.2.4). La restriccion epigrafal $\leq t$ lo convierte en SOCP. $\square$

*Interpretacion financiera.* Este enfoque protege al inversionista contra errores de estimacion en la covarianza. En la practica, se calibra el radio de incertidumbre $\rho$ (reemplazando $\|\mathbf{u}\|_2 \leq 1$ por $\|\mathbf{u}\|_2 \leq \rho$) usando bootstrapping o intervalos de confianza sobre la covarianza muestral. CVXPY resuelve este SOCP directamente.

#### Superficie de Pareto para 3+ objetivos (Boyd & Vandenberghe, 2004, §4.7.5, §6.5)

**Definicion.** Cuando hay $K \geq 3$ objetivos en conflicto (e.g., rendimiento, riesgo, liquidez), una solucion $\mathbf{w}^*$ es **Pareto-optima** si no existe $\mathbf{w}$ factible tal que $f_k(\mathbf{w}) \leq f_k(\mathbf{w}^*)$ para todo $k$ con al menos una desigualdad estricta.

**Metodo de escalarizacion.** La superficie de Pareto se traza resolviendo la familia parametrica:

$$
\min_{\mathbf{w}} \; \lambda_1 \mathbf{w}^\top \Sigma \mathbf{w} - \lambda_2 \boldsymbol{\mu}^\top \mathbf{w} + \lambda_3 \|\mathbf{w}\|_1 \quad \text{s.a.} \quad \mathbf{1}^\top \mathbf{w} = 1, \; \mathbf{w} \geq 0
$$

donde $\lambda_1, \lambda_2, \lambda_3 \geq 0$ con $\lambda_1 + \lambda_2 + \lambda_3 = 1$ ponderan riesgo, rendimiento negativo, y concentracion (proxy de iliquidez). Variando $(\lambda_1, \lambda_2, \lambda_3)$ sobre el simplex unitario se obtiene la **superficie de Pareto** (Boyd & Vandenberghe, 2004, §4.7.5).

*Interpretacion financiera.* Cada punto de la superficie representa un trade-off diferente entre los tres criterios. El comite de inversiones elige el punto que mejor refleja su mandato: un fondo de pensiones ponderara mas $\lambda_1$ (riesgo bajo), mientras que un hedge fund ponderara mas $\lambda_2$ (rendimiento alto).

#### NP-dureza de programacion entera (Boyd & Vandenberghe, 2004, §4.1.3)

**Resultado.** Los problemas de optimizacion con variables enteras ($x \in \mathbb{Z}^n$) son en general **NP-duros**: no se conoce algoritmo de tiempo polinomial para resolverlos. Esto contrasta fundamentalmente con la optimizacion convexa continua, que se resuelve en tiempo polinomial (Boyd & Vandenberghe, 2004, §1.3.2).

*Bosquejo de prueba.* El problema de satisfacibilidad booleana (SAT), que es NP-completo, se reduce en tiempo polinomial a un programa lineal entero binario: cada clausula $(x_i \lor \bar{x}_j \lor x_k)$ se codifica como $x_i + (1-x_j) + x_k \geq 1$ con $x \in \{0,1\}^n$ (Boyd & Vandenberghe, 2004, §4.1.3). $\square$

*Consecuencia practica para la eleccion de herramienta:*

| Tipo de problema | Herramienta | Complejidad |
|-----------------|------------|-------------|
| QP / SOCP / SDP (convexo continuo) | **CVXPY** | Polinomial — $O(n^{3.5})$ |
| MILP / MIP (enteros mixtos) | **Pyomo** + CBC/Gurobi | NP-duro — branch-and-bound exponencial en peor caso |
| MINLP (no lineal + enteros) | **Pyomo** + BONMIN | NP-duro — aun mas costoso |

Esto explica la division de trabajo en el curso: CVXPY para problemas de portafolios (convexos continuos) y Pyomo para problemas de planificacion con variables discretas (dieta, scheduling, seleccion de activos con cardinalidad).

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
