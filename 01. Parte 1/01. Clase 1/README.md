# Clase 1 — Análisis de Acciones con Python

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/01.%20Clase%201/01Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F01.%20Clase%201%2F01Class%20NB.ipynb)

---

## Objetivo

Introducir las herramientas fundamentales de Python para el análisis cuantitativo de acciones: descarga de datos históricos, visualización de precios, cálculo de rendimientos, estimación de volatilidad y evaluación de la distribución de los rendimientos.

---

## 1. Series de tiempo financieras

Una **serie de tiempo financiera** es una secuencia de observaciones de precios o rendimientos indexadas por el tiempo de negociación:

$$
\{S_t\}_{t=0}^{T}
$$

El **precio ajustado de cierre** $S_t^{\text{adj}}$ corrige el precio de mercado por eventos corporativos (splits, dividendos) para que la serie sea comparable a lo largo del tiempo. Es el dato estándar para análisis de rendimientos.

### 1.1 Fuentes de datos

En el notebook usamos el paquete `yfinance`, que descarga datos directamente de Yahoo Finance. Otras fuentes comunes incluyen Bloomberg Terminal, Refinitiv (Thomson Reuters), Alpha Vantage y Quandl.

---

## 2. Hipótesis de Mercados Eficientes (EMH)

La **Hipótesis de Mercados Eficientes** (Fama, 1970) es uno de los pilares de las finanzas modernas. Establece que los precios de los activos reflejan toda la información disponible, de modo que no es posible obtener rendimientos superiores al mercado de forma consistente.

### Tres formas de eficiencia

| Forma | Información incorporada en el precio | Implicación práctica |
|-------|--------------------------------------|---------------------|
| **Débil** | Precios pasados y volumen de transacciones | El análisis técnico (patrones gráficos, medias móviles) no genera rendimientos anormales |
| **Semi-fuerte** | Toda la información pública (estados financieros, noticias, indicadores macro) | El análisis fundamental tampoco genera ventaja sostenida |
| **Fuerte** | Toda la información, incluyendo la privada (*insider information*) | Ni siquiera los insiders pueden obtener ventaja |

**Implicación para este curso**: si la forma débil se cumple, los precios pasados no predicen rendimientos futuros. Esto motiva el uso de modelos estadísticos (media, varianza, covarianza) en lugar de patrones visuales para la construcción de portafolios.

### Evidencia empírica

La evidencia es mixta. Los mercados desarrollados tienden a ser eficientes en forma débil y semi-fuerte, pero existen anomalías documentadas:
- **Efecto momentum** (Jegadeesh & Titman, 1993): activos con buen rendimiento reciente tienden a seguir subiendo a corto plazo.
- **Efecto valor** (Fama & French, 1993): acciones con alto ratio book-to-market tienden a superar al mercado.
- **Efecto calendario**: rendimientos anormalmente altos en enero (*January effect*).

---

## 3. Visualización de precios

### 3.1 Media móvil simple (SMA)

La media móvil simple de ventana $n$ suaviza la serie eliminando ruido de alta frecuencia:

$$
\text{SMA}_t(n) = \frac{1}{n}\sum_{i=0}^{n-1} S_{t-i}
$$

- **SMA corta** (e.g., 20 días): reacciona rápido a cambios recientes.
- **SMA larga** (e.g., 100 o 200 días): captura la tendencia de largo plazo.

**Señales de cruce** (análisis técnico):
- *Golden cross*: SMA corta cruza por encima de SMA larga → señal alcista.
- *Death cross*: SMA corta cruza por debajo de SMA larga → señal bajista.

> Bajo la EMH en forma débil, estas señales no generan rendimientos anormales ajustados por riesgo.

### 3.2 Bandas de Bollinger

Las **Bandas de Bollinger** (Bollinger, 2002) envuelven el precio con una banda de volatilidad:

$$
\text{Upper}_t = \text{SMA}_t(n) + k \cdot \sigma_t(n)
$$
$$
\text{Lower}_t = \text{SMA}_t(n) - k \cdot \sigma_t(n)
$$

donde $\sigma_t(n)$ es la desviación estándar móvil de ventana $n$.

- Con $k = 2$, la banda contiene ≈ 95 % de las observaciones (bajo normalidad).
- Con $k = 1$, contiene ≈ 68 %.
- Cuando las bandas se **estrechan**, indica baja volatilidad (posible movimiento inminente).
- Cuando se **ensanchan**, indica alta volatilidad.

---

## 4. Rendimientos

### 4.1 Rendimiento simple (aritmético)

$$
R_t = \frac{S_t - S_{t-1}}{S_{t-1}} = \frac{S_t}{S_{t-1}} - 1
$$

**Propiedades**:
- Interpretación directa: "el precio subió un 3 %".
- Para un portafolio, el rendimiento es el promedio ponderado: $R_p = \sum_i w_i R_i$.
- **No** es aditivo en el tiempo: $R_{t_0 \to t_2} \neq R_{t_0 \to t_1} + R_{t_1 \to t_2}$.

### 4.2 Rendimiento logarítmico (continuamente compuesto)

$$
r_t = \ln\!\left(\frac{S_t}{S_{t-1}}\right) = \ln(1 + R_t)
$$

**Propiedades**:
- **Aditivo en el tiempo**: $r_{t_0 \to t_n} = \sum_{i=1}^{n} r_{t_{i-1} \to t_i}$.
- **Simétrico**: una ganancia de $+x$ y una pérdida de $-x$ son simétricas en escala log.
- Para rendimientos pequeños ($|R_t| < 0.1$), $r_t \approx R_t$.
- Bajo el modelo GBM, los log-retornos son i.i.d. normales.

### 4.3 Relación entre rendimientos

$$
r_t = \ln(1 + R_t), \qquad R_t = e^{r_t} - 1
$$

El rendimiento acumulado satisface:

$$
\frac{S_T}{S_0} = \prod_{t=1}^{T}(1 + R_t) = \exp\!\left(\sum_{t=1}^{T} r_t\right)
$$

---

## 5. Movimiento Browniano Geométrico (GBM)

El modelo estándar para la dinámica de precios de acciones es el **Movimiento Browniano Geométrico**:

$$
dS_t = \mu \, S_t \, dt + \sigma \, S_t \, dW_t
$$

donde:
- $\mu$: tasa de rendimiento esperado (*drift*).
- $\sigma$: volatilidad instantánea.
- $W_t$: proceso de Wiener estándar (movimiento browniano).

### Solución vía lema de Itô

Aplicando el lema de Itô a $f(S_t) = \ln S_t$:

$$
d\ln S_t = \left(\mu - \frac{\sigma^2}{2}\right)dt + \sigma \, dW_t
$$

Integrando:

$$
\ln S_t - \ln S_{t-1} = \left(\mu - \frac{\sigma^2}{2}\right)\Delta t + \sigma \sqrt{\Delta t} \, Z_t, \qquad Z_t \sim \mathcal{N}(0,1)
$$

Es decir, los **rendimientos logarítmicos son normales**:

$$
r_t \sim \mathcal{N}\!\left(\left(\mu - \frac{\sigma^2}{2}\right)\Delta t,\; \sigma^2 \Delta t\right)
$$

Este resultado es la base del modelo de Black-Scholes-Merton para valoración de opciones (Hull, 2018, Cap. 15).

---

## 6. Volatilidad

### 6.1 Volatilidad histórica anualizada

$$
\hat{\sigma}_{\text{anual}} = \hat{\sigma}_{\text{diario}} \times \sqrt{252}
$$

El factor $\sqrt{252}$ proviene del supuesto de rendimientos i.i.d. y 252 días de negociación por año. Si los rendimientos son independientes, la varianza escala linealmente con el horizonte.

### 6.2 Volatilidad móvil

Se estima con una ventana rodante de $n$ días:

$$
\hat{\sigma}_t(n) = \sqrt{\frac{1}{n-1}\sum_{i=0}^{n-1}(r_{t-i} - \bar{r}_t)^2}
$$

Esto permite observar **cómo cambia la volatilidad** en el tiempo.

### 6.3 Clustering de volatilidad

En la práctica, los rendimientos financieros exhiben **agrupamiento de volatilidad**: períodos de alta volatilidad tienden a ser seguidos por más alta volatilidad, y viceversa. Esto viola el supuesto i.i.d. y motiva los modelos ARCH (Engle, 1982) y GARCH (Bollerslev, 1986).

---

## 7. Distribución de los rendimientos

### 7.1 Hechos estilizados

Los rendimientos financieros presentan características empíricas que se desvían de la distribución normal (Cont, 2001):

1. **Colas pesadas** (leptocurtosis): la curtosis en exceso $\kappa > 0$ indica más observaciones extremas de lo esperado bajo normalidad.
2. **Asimetría negativa**: las caídas grandes son más probables que las subidas equivalentes.
3. **Ausencia de autocorrelación** en rendimientos (pero sí en rendimientos al cuadrado).
4. **Clustering de volatilidad**: períodos de calma y turbulencia se alternan.

### 7.2 Asimetría y curtosis

Para una variable aleatoria $r$ con media $\mu$ y desviación estándar $\sigma$:

$$
\text{Skew}[r] = \mathbb{E}\!\left[\left(\frac{r - \mu}{\sigma}\right)^{\!3}\right]
$$

$$
\text{Kurt}[r] = \mathbb{E}\!\left[\left(\frac{r - \mu}{\sigma}\right)^{\!4}\right] - 3
$$

Para una distribución normal: $\text{Skew} = 0$ y $\text{Kurt} = 0$.

### 7.3 Test de Jarque-Bera

El test de Jarque-Bera evalúa conjuntamente si asimetría y curtosis son compatibles con la distribución normal:

$$
JB = \frac{n}{6}\left(\text{Skew}^2 + \frac{\text{Kurt}^2}{4}\right) \sim \chi^2(2)
$$

Un p-valor $< 0.05$ rechaza la hipótesis nula de normalidad.

### 7.4 QQ-Plot

El **gráfico cuantil-cuantil** compara los cuantiles empíricos de los datos con los cuantiles teóricos de una distribución normal. Si los puntos caen sobre la diagonal, la distribución es aproximadamente normal. Desviaciones en los extremos indican colas pesadas.

---

## 8. Correlación y diversificación

### 8.1 Correlación de Pearson

El coeficiente de correlación lineal entre dos activos $i$ y $j$ es:

$$
\rho_{ij} = \frac{\text{Cov}(r_i, r_j)}{\sigma_i \, \sigma_j}
$$

donde $-1 \leq \rho_{ij} \leq 1$.

### 8.2 Principio de diversificación

La varianza de un portafolio de dos activos:

$$
\sigma_p^2 = w_1^2\sigma_1^2 + w_2^2\sigma_2^2 + 2\,w_1\,w_2\,\rho_{12}\,\sigma_1\,\sigma_2
$$

Cuando $\rho_{12} < 1$, la varianza del portafolio es **menor** que el promedio ponderado de las varianzas individuales. Este es el **principio fundamental de la diversificación** (Markowitz, 1952).

Para $n$ activos, la generalización es:

$$
\sigma_p^2 = \mathbf{w}^\top \boldsymbol{\Sigma} \, \mathbf{w}
$$

donde $\boldsymbol{\Sigma}$ es la matriz de covarianza y $\mathbf{w}$ es el vector de pesos.

---

## Referencias bibliográficas

### Optimización convexa (Boyd & Vandenberghe, 2004)

Los siguientes conceptos del libro *Convex Optimization* se introducen en esta clase y se desarrollan progresivamente en el curso:

- **§2.1–2.2 Conjuntos convexos** (pp. 21–36): El conjunto de portafolios factibles (pesos que suman 1, no negativos) forma un **simplex**, que es un conjunto convexo. Este concepto es fundamental para la optimización de portafolios.
  - Un conjunto C es **convexo** si para todo x, y ∈ C y 0 ≤ θ ≤ 1: θx + (1-θ)y ∈ C
  - El simplex estándar: Δ = {w ∈ ℝⁿ : Σwᵢ = 1, wᵢ ≥ 0}

- **§A.1 Normas** (pp. 635–637): La desviación estándar σ es proporcional a la norma L₂ del vector de desviaciones. Las normas son funciones convexas, lo que garantiza que minimizar riesgo es un problema convexo.

- **§3.1.5 Formas cuadráticas** (pp. 71–72): La varianza del portafolio σ²_p = w'Σw es una **forma cuadrática**. Si Σ es semidefinida positiva (PSD), esta forma es convexa — base de toda la optimización de portafolios.

> **Nota**: El libro completo está disponible gratuitamente en [stanford.edu/~boyd/cvxbook](https://web.stanford.edu/~boyd/cvxbook/).

### Textos principales

- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson.
  - Cap. 15: The Black-Scholes-Merton Model (log-normalidad de precios, GBM).
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
  - Cap. 2: Basic Fixed-Income Securities.
  - Cap. 6–8: Mean-Variance Portfolio Theory.
- **Tsay, R. S.** (2010). *Analysis of Financial Time Series* (3rd ed.). Wiley.
  - Cap. 1: Financial Time Series and Their Characteristics.
  - Cap. 3: Conditional Heteroscedastic Models (ARCH/GARCH).
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos: productos derivados y decisiones económicas bajo incertidumbre* (2a ed.). Cengage Learning.
  - Cubre movimiento browniano, lema de Itô, valoración de derivados y gestión de riesgos desde una perspectiva latinoamericana.
- **McNeil, A. J., Frey, R. & Embrechts, P.** (2015). *Quantitative Risk Management: Concepts, Techniques and Tools* (2nd ed.). Princeton University Press.
  - Cap. 3: Empirical Properties of Financial Data.

### Artículos seminales

- **Fama, E. F.** (1970). Efficient Capital Markets: A Review of Theory and Empirical Work. *The Journal of Finance*, 25(2), 383–417.
- **Markowitz, H.** (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.
- **Engle, R. F.** (1982). Autoregressive Conditional Heteroscedasticity with Estimates of the Variance of United Kingdom Inflation. *Econometrica*, 50(4), 987–1007.
- **Bollerslev, T.** (1986). Generalized Autoregressive Conditional Heteroskedasticity. *Journal of Econometrics*, 31(3), 307–327.
- **Cont, R.** (2001). Empirical Properties of Asset Returns: Stylized Facts and Statistical Issues. *Quantitative Finance*, 1(2), 223–236.
- **Jegadeesh, N. & Titman, S.** (1993). Returns to Buying Winners and Selling Losers. *The Journal of Finance*, 48(1), 65–91.
- **Fama, E. F. & French, K. R.** (1993). Common Risk Factors in the Returns on Stocks and Bonds. *Journal of Financial Economics*, 33(1), 3–56.

### Referencias técnicas

- **Bollinger, J.** (2002). *Bollinger on Bollinger Bands*. McGraw-Hill.
- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — Referencia para las clases de optimización de portafolios (Clases 4, 5, 11).

---

## Recursos adicionales

### Documentación de paquetes

| Paquete | Descripción | Documentación |
|---------|-------------|---------------|
| `yfinance` | Descarga de datos de Yahoo Finance | [github.com/ranaroussi/yfinance](https://github.com/ranaroussi/yfinance) |
| `pandas` | Manipulación de datos tabulares | [pandas.pydata.org](https://pandas.pydata.org/docs/) |
| `numpy` | Cómputo numérico | [numpy.org](https://numpy.org/doc/) |
| `matplotlib` | Visualización | [matplotlib.org](https://matplotlib.org/stable/) |
| `seaborn` | Visualización estadística | [seaborn.pydata.org](https://seaborn.pydata.org/) |
| `scipy.stats` | Distribuciones y tests estadísticos | [docs.scipy.org](https://docs.scipy.org/doc/scipy/reference/stats.html) |

### Cursos y tutoriales en línea

- **MIT OpenCourseWare 18.S096** — *Topics in Mathematics with Applications in Finance*. Disponible en [ocw.mit.edu](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/).
- **Coursera — Financial Engineering and Risk Management** (Columbia University). Cubre media-varianza, opciones y simulación.
- **QuantStart** — Tutoriales de finanzas cuantitativas con Python: [quantstart.com](https://www.quantstart.com/).

### Bases de datos alternativas

| Fuente | Acceso | Cobertura |
|--------|--------|-----------|
| Yahoo Finance (vía `yfinance`) | Gratuito | Acciones, índices, ETFs, criptomonedas |
| Alpha Vantage | API gratuita (con límites) | Acciones, forex, cripto |
| FRED (Federal Reserve) | Gratuito | Tasas de interés, indicadores macro |
| Quandl / Nasdaq Data Link | Freemium | Commodities, futuros, datos alternativos |

---

## Mapa conceptual de la Clase 1

```
Datos de mercado (yfinance)
    │
    ├── Precios ajustados ─── Visualización
    │       │                    ├── Series temporales
    │       │                    ├── Medias móviles (SMA)
    │       │                    └── Bandas de Bollinger
    │       │
    │       └── Rendimientos
    │              ├── Simple: R_t = S_t/S_{t-1} - 1
    │              ├── Logarítmico: r_t = ln(S_t/S_{t-1})
    │              │
    │              ├── Estadísticas descriptivas
    │              │      ├── Media, varianza
    │              │      ├── Asimetría, curtosis
    │              │      └── Jarque-Bera test
    │              │
    │              ├── Volatilidad
    │              │      ├── Histórica anualizada (× √252)
    │              │      ├── Móvil (rolling)
    │              │      └── Clustering (→ ARCH/GARCH)
    │              │
    │              └── Distribución
    │                     ├── Histogramas
    │                     ├── QQ-plots
    │                     ├── Colas pesadas
    │                     └── Normalidad vs. realidad
    │
    └── Correlación ─── Diversificación (→ Markowitz, Clases 2-8)
```

---


## Navegación del curso

→ **Siguiente**: Clase 2: Retornos logarítmicos y matriz de covarianza

---

*Archivo de apoyo para la Clase 1 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
