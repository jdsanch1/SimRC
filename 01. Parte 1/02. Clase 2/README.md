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
- **Semidefinida positiva** (SDP): $\mathbf{x}^\top \boldsymbol{\Sigma} \, \mathbf{x} \geq 0$ para todo $\mathbf{x}$

### Estimador muestral

$$
\hat{\boldsymbol{\Sigma}} = \frac{1}{T-1} \sum_{t=1}^{T} (\mathbf{r}_t - \bar{\mathbf{r}})(\mathbf{r}_t - \bar{\mathbf{r}})^\top
$$

### Varianza del portafolio

Para un portafolio con vector de pesos $\mathbf{w} = (w_1, \ldots, w_n)^\top$:

$$
\sigma_p^2 = \mathbf{w}^\top \boldsymbol{\Sigma} \, \mathbf{w} = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i \, w_j \, \sigma_{ij}
$$

Esta expresión es la base de la **optimización media-varianza** de Markowitz (1952).

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
3. **Portafolios inestables**: pequeños cambios en $\hat{\boldsymbol{\Sigma}}$ producen pesos óptimos muy diferentes.

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

*Archivo de apoyo para la Clase 2 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
