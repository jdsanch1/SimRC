# Clase 2 — Retornos logarítmicos y matriz de covarianza

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/02.%20Clase%202/02Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F02.%20Clase%202%2F02Class%20NB.ipynb)

---

## Objetivo

Extender el análisis de la Clase 1 al caso **multivariado**: calcular rendimientos logarítmicos de múltiples activos, estimar sus matrices de covarianza y correlación, y visualizar las relaciones bivariadas que fundamentan la teoría de portafolios.

---

## 1. Del activo individual al portafolio

En la Clase 1 analizamos activos individuales. En la práctica, los inversionistas mantienen **portafolios** — combinaciones de múltiples activos. Para entender el comportamiento de un portafolio necesitamos no solo los rendimientos y volatilidades individuales, sino las **relaciones entre los activos**.

### Vector de rendimientos

Para $n$ activos, el rendimiento logarítmico en el período $t$ es un vector:

$$
\mathbf{r}_t = (r_{1,t}, \; r_{2,t}, \; \ldots, \; r_{n,t})^\top \in \mathbb{R}^n
$$

### Vector de rendimientos esperados

$$
\boldsymbol{\mu} = \mathbb{E}[\mathbf{r}_t] = (\mu_1, \; \mu_2, \; \ldots, \; \mu_n)^\top
$$

Se estima como la media muestral de cada columna de la matriz de rendimientos.

---

## 2. Matriz de covarianza

### Definición

La **matriz de covarianza** captura tanto la dispersión individual (varianzas en la diagonal) como las relaciones lineales entre pares de activos (covarianzas fuera de la diagonal):

$$
\boldsymbol{\Sigma} = \text{Cov}(\mathbf{r}_t) = \mathbb{E}[(\mathbf{r}_t - \boldsymbol{\mu})(\mathbf{r}_t - \boldsymbol{\mu})^\top]
$$

Para $n$ activos, $\boldsymbol{\Sigma}$ es una matriz $n \times n$ con las siguientes propiedades:

- **Simétrica**: $\sigma_{ij} = \sigma_{ji}$
- **Semidefinida positiva** (SDP): $\mathbf{x}^\top \boldsymbol{\Sigma} \, \mathbf{x} \geq 0$ para todo $\mathbf{x}$, es decir, $\boldsymbol{\Sigma}$ pertenece al cono de matrices semidefinidas positivas $\mathcal{S}^+_n$ (Boyd & Vandenberghe, 2004, §2.4)

**Definición (Matriz semidefinida positiva, Boyd §A.4).** Una matriz simétrica $A \in \mathbb{R}^{n \times n}$ es **semidefinida positiva** ($A \succeq 0$) si y solo si se cumple cualquiera de las siguientes condiciones equivalentes:

1. $\mathbf{x}^\top A \, \mathbf{x} \geq 0$ para todo $\mathbf{x} \in \mathbb{R}^n$.
2. Todos los eigenvalores de $A$ son no negativos: $\lambda_i(A) \geq 0$ para $i = 1, \ldots, n$.
3. Existe una matriz $B$ tal que $A = B^\top B$ (factorización de Cholesky generalizada).

*Prueba de la equivalencia 1 $\Leftrightarrow$ 2 (vía descomposición espectral).* Toda matriz simétrica admite la descomposición $A = Q \Lambda Q^\top$ donde $Q$ es ortogonal y $\Lambda = \text{diag}(\lambda_1, \ldots, \lambda_n)$. Sea $\mathbf{y} = Q^\top \mathbf{x}$; entonces $\mathbf{x}^\top A \, \mathbf{x} = \mathbf{y}^\top \Lambda \, \mathbf{y} = \sum_{i=1}^n \lambda_i y_i^2$. Esta suma es $\geq 0$ para todo $\mathbf{y}$ si y solo si cada $\lambda_i \geq 0$. ∎

*Interpretación financiera*: los eigenvalores de $\boldsymbol{\Sigma}$ son las varianzas de los componentes principales. La condición $\boldsymbol{\Sigma} \succeq 0$ garantiza que ninguna combinación lineal de activos tenga varianza negativa, lo cual es físicamente necesario.

**Proposición (Convexidad de la forma cuadrática, Boyd §3.1.5).** Si $\boldsymbol{\Sigma} \succeq 0$, la función $f(\mathbf{w}) = \mathbf{w}^\top \boldsymbol{\Sigma}\,\mathbf{w}$ es convexa.

*Prueba (método del Hessiano).* El Hessiano de $f$ es $\nabla^2 f(\mathbf{w}) = 2\boldsymbol{\Sigma}$. Una función dos veces diferenciable es convexa si y solo si su Hessiano es semidefinido positivo en todo punto (Boyd §3.1.4). Como $\boldsymbol{\Sigma} \succeq 0$, se tiene $2\boldsymbol{\Sigma} \succeq 0$, luego $f$ es convexa. ∎

*Prueba (método directo).* Para $\mathbf{w}, \mathbf{v} \in \mathbb{R}^n$ y $\theta \in [0,1]$, se verifica expandiendo la forma cuadrática y usando la desigualdad $2\theta(1-\theta)\mathbf{w}^\top\boldsymbol{\Sigma}\,\mathbf{v} \leq \theta(1-\theta)(\mathbf{w}^\top\boldsymbol{\Sigma}\,\mathbf{w} + \mathbf{v}^\top\boldsymbol{\Sigma}\,\mathbf{v})$ (que sigue de $(\mathbf{w}-\mathbf{v})^\top\boldsymbol{\Sigma}(\mathbf{w}-\mathbf{v}) \geq 0$) que $f(\theta\mathbf{w}+(1-\theta)\mathbf{v}) \leq \theta f(\mathbf{w}) + (1-\theta)f(\mathbf{v})$. ∎

*Interpretación financiera*: la convexidad de $\sigma_p^2$ implica que el problema de minimización de riesgo de Markowitz no tiene mínimos locales espurios; todo mínimo local es global, lo que garantiza que los solvers siempre encuentren la solución óptima.

### Estimador muestral

$$
\hat{\boldsymbol{\Sigma}} = \frac{1}{T-1} \sum_{t=1}^{T} (\mathbf{r}_t - \bar{\mathbf{r}})(\mathbf{r}_t - \bar{\mathbf{r}})^\top
$$

### Varianza del portafolio

Para un portafolio con vector de pesos $\mathbf{w} = (w_1, \ldots, w_n)^\top$:

$$
\sigma_p^2 = \mathbf{w}^\top \boldsymbol{\Sigma} \, \mathbf{w} = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i \, w_j \, \sigma_{ij}
$$

Esta forma cuadrática es convexa cuando $\boldsymbol{\Sigma} \succeq 0$ (Boyd & Vandenberghe, 2004, §3.1.5), lo que garantiza que la optimización media-varianza de Markowitz (1952) sea un problema convexo.

### Anualización

Si los rendimientos son diarios e i.i.d., la covarianza anualizada es:

$$
\boldsymbol{\Sigma}_{\text{anual}} = 252 \cdot \boldsymbol{\Sigma}_{\text{diario}}
$$

---

## 3. Matriz de correlación

### Definición

La correlación normaliza la covarianza:

$$
\rho_{ij} = \frac{\sigma_{ij}}{\sigma_i \, \sigma_j}, \qquad -1 \leq \rho_{ij} \leq 1
$$

### Interpretación para portafolios

| $\rho_{ij}$ | Significado | Efecto en portafolio |
|:---:|---|---|
| $\approx 1$ | Activos se mueven juntos | Poca diversificación |
| $\approx 0$ | Movimientos independientes | Buena diversificación |
| $\approx -1$ | Movimientos opuestos | Cobertura natural |

### Principio de diversificación

Para dos activos con pesos iguales ($w = 0.5$):

$$
\sigma_p^2 = 0.25\sigma_1^2 + 0.25\sigma_2^2 + 0.5\rho_{12}\sigma_1\sigma_2
$$

Cuando $\rho_{12} < 1$, siempre se tiene $\sigma_p < 0.5\sigma_1 + 0.5\sigma_2$. La reducción de riesgo es mayor cuanto menor sea la correlación.

---

## 4. Correlación rodante

La correlación entre activos **no es estática**. La correlación rodante de ventana $n$ permite visualizar su evolución:

$$
\hat{\rho}_{ij,t}(n) = \frac{\sum_{k=0}^{n-1}(r_{i,t-k} - \bar{r}_{i,t})(r_{j,t-k} - \bar{r}_{j,t})}{\sqrt{\sum_{k=0}^{n-1}(r_{i,t-k} - \bar{r}_{i,t})^2 \cdot \sum_{k=0}^{n-1}(r_{j,t-k} - \bar{r}_{j,t})^2}}
$$

### Contagio financiero

En períodos de crisis, las correlaciones tienden a **aumentar abruptamente** — un fenómeno conocido como **contagio financiero** (Longin & Solnik, 2001). Esto reduce los beneficios de la diversificación precisamente cuando más se necesitan, y es una de las razones por las que el VaR (Value at Risk) puede subestimar pérdidas extremas.

---

## 5. Coeficiente Beta (CAPM)

La regresión de los rendimientos de un activo $i$ sobre los del mercado $m$ estima el **beta** del CAPM (Sharpe, 1964):

$$
r_{i,t} = \alpha_i + \beta_i \, r_{m,t} + \varepsilon_{i,t}
$$

donde:

$$
\beta_i = \frac{\text{Cov}(r_i, r_m)}{\text{Var}(r_m)}
$$

La estimación de $\beta$ por regresión lineal es el problema de aproximación por mínimos cuadrados más básico (Boyd & Vandenberghe, 2004, §6.1):

$$
\min_{\mathbf{x}} \; \|A\mathbf{x} - \mathbf{b}\|_2^2
$$

**Proposición (Mínimos cuadrados como optimización convexa, Boyd §6.1).** El problema de mínimos cuadrados es un problema de optimización convexa sin restricciones. La función objetivo $g(\mathbf{x}) = \|A\mathbf{x} - \mathbf{b}\|_2^2 = \mathbf{x}^\top A^\top A \, \mathbf{x} - 2\mathbf{b}^\top A \, \mathbf{x} + \mathbf{b}^\top\mathbf{b}$ es convexa porque su Hessiano $\nabla^2 g = 2A^\top A \succeq 0$ (toda matriz de la forma $A^\top A$ es SDP). La condición de primer orden $\nabla g = 2A^\top A\mathbf{x} - 2A^\top\mathbf{b} = \mathbf{0}$ produce las **ecuaciones normales** $A^\top A\,\mathbf{x} = A^\top\mathbf{b}$, cuya solución es $\hat{\mathbf{x}} = (A^\top A)^{-1}A^\top\mathbf{b}$ cuando $A$ tiene rango completo.

*Interpretación financiera*: al estimar $\beta_i$ por OLS, estamos resolviendo un problema convexo que siempre tiene solución global. Esto garantiza que la descomposición del riesgo en sistemático ($\beta$) e idiosincrático ($\varepsilon$) es única y óptima en el sentido de mínima varianza.

### Interpretación

| $\beta$ | Significado |
|:---:|---|
| $\beta > 1$ | Activo más volátil que el mercado (agresivo) |
| $\beta = 1$ | Se mueve con el mercado |
| $0 < \beta < 1$ | Menos volátil que el mercado (defensivo) |
| $\beta < 0$ | Se mueve en dirección opuesta al mercado |

El **riesgo sistemático** (no diversificable) de un activo queda capturado por $\beta$, mientras que $\varepsilon$ representa el riesgo idiosincrático (diversificable).

---

## 6. Problemas de la covarianza muestral

La estimación muestral $\hat{\boldsymbol{\Sigma}}$ tiene problemas conocidos, especialmente cuando $n$ (número de activos) es grande relativo a $T$ (observaciones):

1. **Error de estimación**: con $n$ activos hay $n(n+1)/2$ parámetros a estimar, lo que genera inestabilidad.
2. **Sensibilidad a outliers**: valores extremos pueden distorsionar las estimaciones.
3. **Portafolios inestables**: pequeños cambios en $\hat{\boldsymbol{\Sigma}}$ producen pesos óptimos muy diferentes. En particular, cuando la covarianza muestral no es estrictamente definida positiva, se pierde la garantía de solución única en la optimización (Boyd & Vandenberghe, 2004, §A.4).

Estos problemas motivan los **estimadores robustos** que se estudiarán en las Clases 5 y 6:
- **Shrunk Covariance** (Clase 5): contrae la covarianza muestral hacia una estructura más estable.
- **Estimador de Huber** (Clase 6): estima la media de forma robusta a outliers.

---

## 7. Visualización de relaciones entre activos

### Herramientas clave

| Gráfico | Qué muestra | Cuándo usar |
|---------|-------------|-------------|
| **Heatmap de correlación** | $\rho_{ij}$ para todos los pares | Visión global de co-movimiento |
| **Scatter matrix / pairplot** | Dispersión bivariada + KDE marginal | Exploración de dependencias no lineales |
| **Jointplot** | Dispersión + marginales + KDE conjunta | Análisis detallado de un par |
| **Regplot** | Dispersión + recta de regresión | Estimar $\beta$ visualmente |
| **Rolling correlation** | $\rho_{ij}(t)$ en el tiempo | Detectar cambios de régimen |

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §2.4 (conos semidefinidos positivos), §3.1.5 (formas cuadráticas), §6.1 (mínimos cuadrados), §A.4 (matrices PSD).

- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson.
  - Cap. 22: Estimating Volatilities and Correlations.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
  - Cap. 6–8: Mean-Variance Portfolio Theory.
- **Tsay, R. S.** (2010). *Analysis of Financial Time Series* (3rd ed.). Wiley.
  - Cap. 1–2: Financial Time Series and Their Characteristics; Linear Time Series.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos: productos derivados y decisiones económicas bajo incertidumbre* (2a ed.). Cengage Learning.
  - Cubre procesos estocásticos, derivados y gestión de riesgos.
- **McNeil, A. J., Frey, R. & Embrechts, P.** (2015). *Quantitative Risk Management* (2nd ed.). Princeton University Press.
  - Cap. 3: Empirical Properties of Financial Data.

### Artículos seminales

- **Markowitz, H.** (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.
- **Sharpe, W. F.** (1964). Capital Asset Prices: A Theory of Market Equilibrium under Conditions of Risk. *The Journal of Finance*, 19(3), 425–442.
- **Engle, R. F.** (1982). Autoregressive Conditional Heteroscedasticity. *Econometrica*, 50(4), 987–1007.
- **Cont, R.** (2001). Empirical Properties of Asset Returns: Stylized Facts and Statistical Issues. *Quantitative Finance*, 1(2), 223–236.
- **Longin, F. & Solnik, B.** (2001). Extreme Correlation of International Equity Markets. *The Journal of Finance*, 56(2), 649–676.
- **Fama, E. F.** (1970). Efficient Capital Markets. *The Journal of Finance*, 25(2), 383–417.

---

## Recursos adicionales

### Documentación de paquetes

| Paquete | Uso en esta clase | Documentación |
|---------|-------------------|---------------|
| `yfinance` | Descarga de datos | [github.com/ranaroussi/yfinance](https://github.com/ranaroussi/yfinance) |
| `pandas` | `.cov()`, `.corr()`, `.rolling()` | [pandas.pydata.org](https://pandas.pydata.org/docs/) |
| `numpy` | `np.log()`, operaciones matriciales | [numpy.org](https://numpy.org/doc/) |
| `seaborn` | `heatmap`, `pairplot`, `regplot` | [seaborn.pydata.org](https://seaborn.pydata.org/) |
| `scipy.stats` | Distribuciones, ajuste normal | [docs.scipy.org](https://docs.scipy.org/doc/scipy/reference/stats.html) |

### Conexión con otras clases

| Clase | Relación con Clase 2 |
|-------|---------------------|
| **Clase 1** | Fundamentos: rendimientos, volatilidad, distribución |
| **Clase 3** | Usa $\boldsymbol{\Sigma}$ para simular la frontera eficiente con Monte Carlo |
| **Clase 4** | Maximiza el ratio de Sharpe usando $\boldsymbol{\mu}$ y $\boldsymbol{\Sigma}$ |
| **Clase 5** | Reemplaza $\hat{\boldsymbol{\Sigma}}$ muestral por Shrunk Covariance |
| **Clase 6** | Reemplaza $\bar{\mathbf{r}}$ muestral por el estimador de Huber |
| **Clase 11** | Optimización cuadrática con CVXPY usando $\boldsymbol{\Sigma}$ |

---

## Mapa conceptual de la Clase 2

```
Precios de cierre (yfinance)
    │
    └── Rendimientos logarítmicos r = ln(S_t/S_{t-1})
            │
            ├── Estadísticas descriptivas
            │      ├── Media (μ)
            │      ├── Varianza (σ²)
            │      ├── Asimetría, curtosis
            │      └── Distribución vs. normal
            │
            ├── Covarianza (Σ)
            │      ├── Muestral: (1/(T-1)) Σ(r-r̄)(r-r̄)'
            │      ├── Anualizada: × 252
            │      └── → Varianza de portafolio: w'Σw
            │
            ├── Correlación (ρ)
            │      ├── Heatmap
            │      ├── Rodante (rolling)
            │      └── → Diversificación
            │
            ├── Beta (CAPM)
            │      ├── β = Cov(rᵢ, rₘ) / Var(rₘ)
            │      └── → Riesgo sistemático
            │
            └── Visualización bivariada
                   ├── Pairplot / scatter matrix
                   ├── Jointplot (KDE conjunta)
                   └── Regplot (recta de regresión)
```

---


## Navegación del curso

← **Anterior**: Clase 1: Análisis de acciones  
→ **Siguiente**: Clase 3: Opciones financieras

---

*Archivo de apoyo para la Clase 2 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
