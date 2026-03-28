# Clase 9 — Optimización Monte Carlo refinada

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/09.%20Clase%209/09Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F09.%20Clase%209%2F09Class%20NB.ipynb)

---

## Objetivo

Refinar la simulación Monte Carlo de portafolios incorporando estimadores robustos (Huber + Ledoit-Wolf) y comparar con la optimización determinista de Markowitz.

---

## Contenido teórico

### Simulación Monte Carlo de portafolios

Se generan N portafolios con pesos aleatorios y se evalúa el rendimiento y riesgo de cada uno usando estimadores robustos.

**Distribución de Dirichlet para pesos aleatorios.** Los pesos se generan con $\mathbf{w} \sim \text{Dirichlet}(\mathbf{1}_n)$, que produce vectores uniformemente distribuidos en el simplex $\Delta_n = \{\mathbf{w} \geq 0, \sum w_i = 1\}$. Para cada portafolio se calcula:

$$
\mu_p = 252 \, \hat{\boldsymbol{\mu}}^\top \mathbf{w}, \qquad \sigma_p = \sqrt{252 \, \mathbf{w}^\top \hat{\Sigma} \, \mathbf{w}}
$$

donde $\hat{\boldsymbol{\mu}}$ es el estimador de Huber (Clase 6) y $\hat{\Sigma}$ el de Ledoit-Wolf (Clase 5).

En la práctica, los portafolios pueden tener restricciones adicionales (límites sectoriales, posiciones máximas, turnover) que, al ser lineales, preservan la convexidad del QP (Boyd & Vandenberghe, 2004, §4.4). Restricciones cuadráticas como el tracking error convierten el problema en un QCQP que sigue siendo convexo (Boyd & Vandenberghe, 2004, §4.6).

### Comparación MC vs. optimización

| Método | Ventaja | Limitación |
|--------|---------|------------|
| Monte Carlo | Explora todo el espacio factible | Ineficiente para encontrar el óptimo |
| Markowitz (QP) | Encuentra el óptimo exacto (Boyd & Vandenberghe, 2004, §4.4) | Sensible a errores de estimación |
| MC + estimadores robustos | Explora con parámetros estables | No garantiza optimalidad |

#### Preservacion de convexidad bajo restricciones lineales (Boyd & Vandenberghe, 2004, §4.4)

**Teorema (QP con restricciones lineales).** Sea $f(\mathbf{w}) = \mathbf{w}^\top \Sigma \mathbf{w}$ con $\Sigma \succeq 0$. El problema

$$
\min_{\mathbf{w}} \; \mathbf{w}^\top \Sigma \mathbf{w} \quad \text{s.a.} \quad A\mathbf{w} = b, \; G\mathbf{w} \leq h
$$

es un QP convexo. La interseccion de un numero finito de semiespacios y planos (restricciones lineales) es un **poliedro**, que es un conjunto convexo. Como la funcion objetivo es cuadratica convexa y el dominio factible es convexo, el problema global es convexo y todo minimo local es global.

*Bosquejo de prueba.* Un semiplano $\{w : g_i^\top w \leq h_i\}$ es convexo (la desigualdad preserva convexidad al ser $g_i^\top w$ afin). La interseccion finita de conjuntos convexos es convexa. La composicion de una funcion convexa sobre un dominio convexo da un programa convexo (Boyd & Vandenberghe, 2004, Prop. 4.2.1). $\square$

*Interpretacion financiera.* Las restricciones tipicas de portafolios son lineales y por tanto preservan la convexidad del QP de Markowitz:

| Restriccion | Formulacion | Tipo |
|-------------|------------|------|
| Limites sectoriales | $\sum_{i \in S_k} w_i \leq u_k$ | Desigualdad lineal |
| Posicion maxima | $w_i \leq w_{\max}$ | Cota superior |
| Turnover | Suma de cambios absolutos ≤ τ (se linealiza) | Desigualdad lineal |

#### QCQP para tracking error (Boyd & Vandenberghe, 2004, §4.6)

Cuando se agrega una restriccion de tracking error respecto a un benchmark $\mathbf{b}$, el problema se convierte en un **QCQP** (Quadratically Constrained Quadratic Program):

$$
\min_{\mathbf{w}} \; \mathbf{w}^\top \Sigma \mathbf{w} \quad \text{s.a.} \quad (\mathbf{w} - \mathbf{b})^\top \Sigma (\mathbf{w} - \mathbf{b}) \leq \mathrm{TE}_{\max}^2, \quad \mathbf{1}^\top \mathbf{w} = 1, \quad \mathbf{w} \geq 0
$$

Este problema es convexo porque cada restriccion cuadratica $f_i(\mathbf{w}) = \mathbf{w}^\top P_i \mathbf{w} + q_i^\top \mathbf{w} + r_i \leq 0$ define un conjunto convexo cuando $P_i \succeq 0$ (el conjunto subnivel de una funcion convexa es convexo, Boyd & Vandenberghe, 2004, §3.1.6). Aqui $P_i = \Sigma \succeq 0$, asi que la restriccion de tracking error es convexa.

#### Metodos de punto interior (Boyd & Vandenberghe, 2004, §11.1)

Los solvers que usa CVXPY (ECOS, SCS, MOSEK) implementan **metodos de punto interior**. La idea central es reemplazar las restricciones de desigualdad por una **funcion barrera logaritmica**:

$$
\min_{\mathbf{w}} \; t \cdot f_0(\mathbf{w}) - \sum_{i=1}^{m} \log(-f_i(\mathbf{w}))
$$

donde $f_i(\mathbf{w}) \leq 0$ son las restricciones y $t > 0$ es un parametro que crece iterativamente. Cuando $t \to \infty$, la barrera penaliza infinitamente las violaciones de restricciones, y la solucion converge al optimo del problema original. La complejidad es $O(\sqrt{m} \log(1/\epsilon))$ iteraciones de Newton, cada una con costo $O(n^3)$, dando complejidad total $O(n^{3.5})$ para QPs tipicos. Esto explica por que los solvers resuelven portafolios con cientos de activos en fracciones de segundo.

---

## Referencias bibliográficas

### Textos principales

- **Charnes, A. & Cooper, W. W.** (1962). Programming with linear fractional functionals. *Naval Research Logistics Quarterly*, 9(3–4), 181–186.
- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §4.4 (QP con restricciones), §4.6 (QCQP), §11.1 (métodos de punto interior usados por los solvers de CVXPY).
- **Glasserman, P.** (2003). *Monte Carlo Methods in Financial Engineering*. Springer.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

---

## Recursos adicionales

### Documentación

| Recurso | Descripción |
|---------|-------------|
| [CVXPY](https://www.cvxpy.org/) | Optimización convexa (DCP) |
| [sklearn.covariance.LedoitWolf](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html) | Covarianza robusta |
| [numpy.random.dirichlet](https://numpy.org/doc/stable/reference/random/generated/numpy.random.dirichlet.html) | Generación de pesos aleatorios |

### Conexión con otras clases

| Clase | Relación |
|-------|----------|
| **Clase 4** | Frontera eficiente y Sharpe con CVXPY |
| **Clase 5** | Covarianza robusta (Ledoit-Wolf) usada aquí |
| **Clase 6** | Media robusta (Huber) usada aquí |
| **Clase 7** | VaR/CVaR como medidas de riesgo alternativas |
| **Clase 10** | Extiende con activo libre de riesgo (bono) |
| **Clase 11** | Frontera eficiente con `portfolio_func.py` reutilizable |

---

## Navegación del curso

← **Anterior**: Clase 8: Resumen Parte 1
→ **Siguiente**: Clase 10: Inclusión de activo libre de riesgo

---

*Archivo de apoyo para la Clase 9 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
