# Clase 14 — Opciones barrera (knock-in / knock-out)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/14.%20Clase%2014/14Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F14.%20Clase%2014%2F14Class%20NB.ipynb)

---

## Objetivo

Introducir las **opciones barrera** (path-dependent) y su valuación por simulación Monte Carlo. A diferencia de las opciones europeas (Clase 3 y 8), el payoff depende de toda la trayectoria del precio, no solo del valor final.

---

## Contenido teórico

### Tipos de opciones barrera

| Tipo | Activación | Efecto |
|------|-----------|--------|
| **Knock-in** | Precio toca la barrera | La opción se **activa** |
| **Knock-out** | Precio toca la barrera | La opción se **desactiva** |
| **Up** | Barrera por encima del spot | Monitorea subidas |
| **Down** | Barrera por debajo del spot | Monitorea caídas |

### Valuación por Monte Carlo

Las opciones barrera no tienen solución analítica simple (a diferencia de Black-Scholes para europeas). La simulación Monte Carlo es el método estándar:

1. Generar N trayectorias completas del precio
2. Para cada trayectoria, verificar si la barrera fue tocada
3. Calcular el payoff condicional
4. Promediar y descontar

#### Operaciones que preservan convexidad y sus limites (Boyd & Vandenberghe, 2004, §3.2)

La valuacion de opciones involucra composiciones de funciones. El siguiente cuadro resume las operaciones que preservan (o rompen) la convexidad, con ejemplos financieros:

| Operacion | Preserva convexidad? | Ejemplo financiero |
|-----------|---------------------|-------------------|
| $\max(f(x), 0)$ con $f$ convexa | Si (Boyd §3.2.3) | Payoff de call europeo: $\max(S_T - K, 0)$ |
| Suma ponderada positiva (αᵢ ≥ 0) | Sí (Boyd §3.2.1) | Portafolio de calls: $\sum n_i \max(S_T - K_i, 0)$ |
| Composicion $h(g(x))$ con $h$ convexa no-decreciente, $g$ convexa | Si (Boyd §3.2.4) | $\exp(\mathbf{w}^\top \Sigma \mathbf{w})$: riesgo exponencial |
| Supremo $\sup_\alpha f(x, \alpha)$ | Si (Boyd §3.2.3) | Worst-case loss: $\max_i \text{Loss}_i(\mathbf{w})$ |
| Producto con función indicadora | **No en general** | Payoff de opcion barrera: $\max(S_T-K,0) \cdot \mathbf{1}_{\{\max_t S_t > B\}}$ |
| Minimo $\min(f(x), g(x))$ | **No** (pero el maximo si) | Cap + floor combinado |

**Resultado clave: la funcion indicadora de barrera rompe la convexidad.** El payoff de una opcion knock-in es:

$$
V = e^{-rT} \max(S_T - K, 0) \cdot \mathbf{1}\left\{\max_{0 \leq t \leq T} S_t \geq B\right\}
$$

Aunque $\max(S_T - K, 0)$ es convexa en $S_T$, el producto con la indicadora $\mathbf{1}\{\max_t S_t \geq B\}$ no preserva convexidad porque la indicadora es discontinua y no es convexa ni concava (Boyd & Vandenberghe, 2004, §3.2). Esto explica por que la optimizacion de portafolios de opciones barrera **no se puede resolver con solvers convexos** y requiere simulacion Monte Carlo.

#### Calibracion como aproximacion convexa (Boyd & Vandenberghe, 2004, §6.1)

Aunque la valuacion directa de derivados exoticos no es convexa, la **calibracion de modelos** si puede formularse como un problema de optimizacion convexa. Dado un conjunto de precios de mercado $\{V_i^{\text{mkt}}\}$ y un modelo parametrico $V_i(\boldsymbol{\theta})$, la calibracion por minimos cuadrados:

$$
\min_{\boldsymbol{\theta}} \; \sum_{i=1}^{m} \left( V_i(\boldsymbol{\theta}) - V_i^{\text{mkt}} \right)^2
$$

es convexa cuando $V_i(\boldsymbol{\theta})$ es afin en $\boldsymbol{\theta}$ (como en el caso de interpolacion de superficies de volatilidad implicita con funciones base lineales). Para modelos no lineales (Heston, SABR), se usan **aproximaciones convexas** locales (linearizacion de Taylor) dentro de algoritmos iterativos tipo Gauss-Newton (Boyd & Vandenberghe, 2004, §6.1.1). Cada paso del algoritmo resuelve un subproblema de minimos cuadrados convexo, garantizando convergencia local.

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §3.2 (operaciones que preservan convexidad), §6.1–6.2 (aproximación y calibración).
- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson. — Cap. 26: Exotic Options.
- **Glasserman, P.** (2003). *Monte Carlo Methods in Financial Engineering*. Springer. — Cap. 6: Barrier options.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning. — Cap. 8: Opciones exóticas.

---

## Navegación del curso

← **Anterior**: Clase 13: Portafolio con bono
→ **Siguiente**: Clase 15: Programación estocástica

---

*Archivo de apoyo para la Clase 14 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
