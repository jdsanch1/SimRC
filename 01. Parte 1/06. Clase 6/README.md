# Clase 6 — Media robusta (estimador de Huber) y generación de números aleatorios

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/06.%20Clase%206/06Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F06.%20Clase%206%2F06Class%20NB.ipynb)

---

## Objetivo

Introducir el **estimador de Huber** como alternativa robusta a la media muestral para estimar rendimientos esperados en presencia de outliers. Revisar los fundamentos de **generación de números pseudoaleatorios** (LCG, Box-Muller) como base para la simulación Monte Carlo de portafolios.

---

## 1. El problema de la media muestral

### Sensibilidad a outliers

La media muestral minimiza la suma de errores al cuadrado:

$$
\bar{r} = \arg\min_\mu \sum_{t=1}^{T} (r_t - \mu)^2
$$

La penalización cuadrática da peso **desproporcionado** a observaciones extremas. En mercados financieros, un solo día de crash puede sesgar la media de meses de datos.

### Punto de quiebre (breakdown point)

El **punto de quiebre** mide la proporción de datos que pueden ser arbitrariamente contaminados antes de que el estimador se vuelva inútil:

| Estimador | Punto de quiebre |
|---|---|
| Media muestral | 0% (un solo outlier la destruye) |
| Mediana | 50% (máximo posible) |
| Huber | Configurable vía c (típicamente 5–25%) |

El estimador de Huber ofrece un **compromiso** entre eficiencia bajo normalidad y robustez ante outliers.

---

## 2. Estimador de Huber

### Función de pérdida

Huber (1964) propone una pérdida **híbrida**: cuadrática para residuos pequeños, lineal para grandes. Boyd & Vandenberghe (2004, §6.1.2) la clasifican como función convexa y la implementan en CVXPY como `cp.huber(x, M)`:

$$
\rho_c(x) = \begin{cases} \frac{1}{2}x^2 & \text{si } |x| \leq c \\\\ c|x| - \frac{1}{2}c^2 & \text{si } |x| > c \end{cases}
$$

donde c > 0 es el **parámetro de corte** (tuning constant).

**Definición (Penalización de Huber, Boyd Eq. 6.9, p. 294).** Boyd & Vandenberghe (2004, §6.1.2) definen la función de Huber con la notación $\phi_{\text{hub}}$:

$$
\phi_{\text{hub}}(x) = \begin{cases} x^2 & |x| \leq M \\ 2M|x| - M^2 & |x| > M \end{cases}
$$

donde $M > 0$ es el parámetro de umbral. La correspondencia con la notación estadística clásica es: $\phi_{\text{hub}}(x) = 2\rho_M(x)$ y el parámetro $M$ de Boyd corresponde al $c$ de Huber (1964). En CVXPY se invoca como `cp.huber(x, M)`.

*Prueba de convexidad (Boyd §3.1.4).* Para $|x| < M$, $\phi''(x) = 2 \geq 0$. Para $|x| > M$, $\phi''(x) = 0 \geq 0$. En $x = \pm M$, la derivada $\phi'$ es continua: $\phi'(M^-) = 2M = \phi'(M^+)$. Una función con segunda derivada no negativa y derivada continua es convexa. $\blacksquare$

**Comparación de funciones de pérdida (Boyd §6.1, pp. 293–295):**

| Pérdida | Influencia $\phi'(u)$ | Eficiencia (normalidad) | Punto de quiebre |
|---|---|---|---|
| **Cuadrática** $u^2$ | $2u$ — ilimitada | 100% | 0% |
| **Huber** | Acotada por $\pm 2M$ | 95% (con $M = 1.345\sigma$) | ~5–25% |
| **Valor absoluto** $\|u\|$ | $\text{sign}(u)$ — discontinua | 64% | 50% |

El estimador de Huber ocupa el punto óptimo del tradeoff eficiencia-robustez: casi tan eficiente como la media bajo normalidad, pero resistente a outliers.

### Función de influencia (ψ)

La derivada de ρ define la función de influencia:

$$
\psi_c(x) = \begin{cases} x & \text{si } |x| \leq c \\\\ c \cdot \text{sign}(x) & \text{si } |x| > c \end{cases}
$$

La función de influencia está **acotada**: ninguna observación, por extrema que sea, puede tener una influencia mayor que c. En contraste, la media muestral tiene ψ(x) = x (influencia ilimitada). El estimador de Huber se interpreta como un problema de regresión regularizado donde los residuos grandes se penalizan linealmente en vez de cuadráticamente, logrando el compromiso óptimo entre eficiencia (L₂) y robustez (L₁) (Boyd & Vandenberghe, 2004, §6.4).

### Parámetro de corte c

- **c = 1.345**: eficiencia del 95% bajo normalidad. Valor por defecto en la mayoría de implementaciones.
- **c → ∞**: se recupera la media muestral.
- **c → 0**: se aproxima a la mediana.

### Implementación

En Python, `statsmodels.robust.scale.Huber()` estima simultáneamente la media y la escala de forma robusta:

```python
import statsmodels.api as sm
huber = sm.robust.scale.Huber()
mu_robust, scale_robust = huber(data)
```

---

## 3. Estimadores robustos en portafolios

### Combinación Huber + Ledoit-Wolf

Para la optimización de portafolios se necesitan dos insumos:

| Insumo | Estimador clásico | Estimador robusto | Clase |
|---|---|---|---|
| Rendimiento esperado μ | Media muestral | **Huber** | Clase 6 |
| Covarianza Σ | Muestral | **Ledoit-Wolf** | Clase 5 |

La combinación de ambos estimadores robustos produce portafolios más **estables** y con mejor desempeño fuera de muestra.

### En `portfolio_func.py`

Las funciones `optimal_portfolio()` y `sim_mont_portfolio()` del curso ya usan internamente:
- `sm.robust.scale.Huber()` para estimar μ
- `sklearn.covariance.ShrunkCovariance()` para estimar Σ

---

## 4. Generación de números pseudoaleatorios

### Generador Congruencial Lineal (LCG)

El LCG genera una secuencia de enteros mediante:

$$
x_{n+1} = (a \cdot x_n + c) \mod m
$$

Los números uniformes en [0, 1) se obtienen como u_n = x_n / m.

**Generador mínimo estándar** (Park & Miller, 1988): m = 2³¹ - 1, a = 16807, c = 0.

### Propiedades de los LCG

| Propiedad | Descripción |
|---|---|
| **Período** | Máximo m (si los parámetros son bien elegidos) |
| **Velocidad** | Muy rápido (una multiplicación + módulo) |
| **Limitación** | Correlación en dimensiones altas (ej. RANDU de IBM) |
| **Uso actual** | Base para generadores más sofisticados (Mersenne Twister) |

### Método de Box-Muller

Transforma dos uniformes independientes U₁, U₂ en dos normales estándar:

$$
Z_1 = \sqrt{-2\ln(1 - U_1)} \cos(2\pi U_2)
$$

$$
Z_2 = \sqrt{-2\ln(1 - U_1)} \sin(2\pi U_2)
$$

Esto permite generar rendimientos normales para simulación Monte Carlo.

### Conexión con Monte Carlo

La simulación Monte Carlo de portafolios requiere:
1. Generar pesos aleatorios (distribución de Dirichlet)
2. Generar rendimientos aleatorios (normales multivariados)
3. Evaluar el rendimiento y riesgo de cada portafolio simulado

Los métodos de esta clase (LCG → Box-Muller → normales) son los **bloques fundamentales** de estas simulaciones.

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §6.1.2 (penalización de Huber), §6.4 (regularización).
- **Huber, P. J. & Ronchetti, E. M.** (2009). *Robust Statistics* (2nd ed.). Wiley.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press. — Cap. 6–8.
- **Tsay, R. S.** (2010). *Analysis of Financial Time Series* (3rd ed.). Wiley.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

### Artículos seminales

- **Huber, P. J.** (1964). Robust Estimation of a Location Parameter. *The Annals of Mathematical Statistics*, 35(1), 73–101.
- **Box, G. E. P. & Muller, M. E.** (1958). A Note on the Generation of Random Normal Deviates. *The Annals of Mathematical Statistics*, 29(2), 610–611.
- **Ledoit, O. & Wolf, M.** (2004). A well-conditioned estimator for large-dimensional covariance matrices. *Journal of Multivariate Analysis*, 88(2), 365–411.
- **Markowitz, H.** (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.
- **Michaud, R. O.** (1989). The Markowitz Optimization Enigma. *Financial Analysts Journal*, 45(1), 31–42.
- **Park, S. K. & Miller, K. W.** (1988). Random Number Generators: Good Ones Are Hard To Find. *Communications of the ACM*, 31(10), 1192–1201.

---

## Recursos adicionales

### Documentación

| Recurso | Descripción |
|---------|-------------|
| [statsmodels.robust.scale.Huber](https://www.statsmodels.org/stable/generated/statsmodels.robust.scale.Huber.html) | Estimador de Huber en statsmodels |
| [sklearn.covariance.LedoitWolf](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html) | Covarianza robusta Ledoit-Wolf |
| [numpy.random](https://numpy.org/doc/stable/reference/random/) | Generadores de NumPy (Mersenne Twister, PCG64) |

### Conexión con otras clases

| Clase | Relación |
|-------|----------|
| **Clase 5** | Estimador robusto de Σ (Shrunk Covariance / Ledoit-Wolf) |
| **Clase 7** | Comparación de estimadores (muestral vs. robusto) en análisis de riesgo |
| **Clase 9** | Simulación Monte Carlo refinada usando estimadores robustos |
| **Clase 11** | Frontera eficiente con `portfolio_func` (usa Huber + Shrunk internamente) |

---

## Mapa conceptual de la Clase 6

```
Estimación de μ (rendimiento esperado)
    │
    ├── Media muestral
    │     └── Problema: sensible a outliers (breakdown = 0%)
    │
    ├── Estimador de Huber
    │     ├── Pérdida híbrida: cuadrática + lineal
    │     ├── Parámetro c controla robustez vs. eficiencia
    │     ├── ψ acotada → influencia limitada
    │     └── → Usa en portfolio_func.py
    │
    └── Combinación robusta
          ├── μ: Huber (Clase 6)
          ├── Σ: Ledoit-Wolf (Clase 5)
          └── → Portafolios más estables

Generación de números aleatorios
    │
    ├── LCG: x_{n+1} = (a·x_n + c) mod m
    │     ├── Park-Miller (mínimo estándar)
    │     └── RANDU (ejemplo de mal generador)
    │
    ├── Box-Muller: U(0,1) → N(0,1)
    │     └── Z = √(-2ln(1-U₁))·cos(2πU₂)
    │
    └── → Simulación Monte Carlo (Clase 9)
```

---


## Navegación del curso

← **Anterior**: Clase 5: Covarianza robusta  
→ **Siguiente**: Clase 7: Comparación de estimadores y riesgo

---

*Archivo de apoyo para la Clase 6 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
