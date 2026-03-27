# Clase 4 — Ratio de Sharpe y portafolio óptimo

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/04.%20Clase%204/04Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F04.%20Clase%204%2F04Class%20NB.ipynb)

---

## Objetivo

Formular y resolver el problema de **selección óptima de portafolios**: encontrar los pesos que maximizan el rendimiento ajustado por riesgo (ratio de Sharpe) y trazar la frontera eficiente de Markowitz, todo mediante **optimización convexa con CVXPY** (enfoque DCP).

---

## 1. Rendimiento y riesgo de un portafolio

Para un portafolio de n activos con pesos w, rendimientos esperados μ y matriz de covarianza Σ:

**Rendimiento esperado:**

$$
\mu_p = \mathbf{w}^\top \boldsymbol{\mu} = \sum_{i=1}^{n} w_i \, \mu_i
$$

**Varianza (riesgo al cuadrado):**

$$
\sigma_p^2 = \mathbf{w}^\top \boldsymbol{\Sigma} \, \mathbf{w} = \sum_{i=1}^{n} \sum_{j=1}^{n} w_i \, w_j \, \sigma_{ij}
$$

**Restricciones básicas:**

$$
\sum_{i=1}^{n} w_i = 1, \qquad w_i \geq 0 \text{ (sin ventas en corto)}
$$

---

## 2. Ratio de Sharpe

### Definición

El **ratio de Sharpe** (Sharpe, 1966) mide el **rendimiento en exceso por unidad de riesgo**:

$$
S = \frac{\mu_p - r_f}{\sigma_p}
$$

donde r\_f es la tasa libre de riesgo.

### Interpretación

| Valor de S | Interpretación |
|:---:|---|
| S > 1 | Buena relación rendimiento/riesgo |
| S > 2 | Excelente |
| S < 0 | El portafolio rinde menos que la tasa libre de riesgo |

### Portafolio tangente

El portafolio que **maximiza el ratio de Sharpe** se llama **portafolio tangente**. Geométricamente, es el punto de la frontera eficiente donde la línea desde la tasa libre de riesgo es tangente a la frontera.

---

## 3. Frontera eficiente de Markowitz

### Definición

La **frontera eficiente** (Markowitz, 1952) es el conjunto de portafolios que ofrecen el máximo rendimiento esperado para cada nivel de riesgo.

### Formulación como QP

Para cada rendimiento objetivo μ*:

$$
\min_{\mathbf{w}} \quad \mathbf{w}^\top \boldsymbol{\Sigma} \, \mathbf{w}
$$

sujeto a:

$$
\boldsymbol{\mu}^\top \mathbf{w} = \mu^*, \qquad \sum_i w_i = 1, \qquad w_i \geq 0
$$

Este es un **problema cuadrático convexo** (QP): objetivo cuadrático convexo con restricciones lineales.

### Portafolio de mínima varianza (MVP)

El punto más a la izquierda de la frontera es el **portafolio de mínima varianza global**:

$$
\min_{\mathbf{w}} \quad \mathbf{w}^\top \boldsymbol{\Sigma} \, \mathbf{w} \qquad \text{s.a.} \quad \sum_i w_i = 1, \quad w_i \geq 0
$$

---

## 4. Optimización con CVXPY (DCP)

### Programación Convexa Disciplinada

CVXPY utiliza el paradigma **DCP** (Disciplined Convex Programming) para verificar automáticamente la convexidad:

| Expresión CVXPY | Tipo DCP | Válida en |
|---|---|---|
| `cp.quad_form(w, Σ)` | Convexa | Objetivo (minimizar) |
| `μ @ w` | Afín | Objetivo o restricción |
| `cp.sum(w) == 1` | Afín | Restricción de igualdad |
| `w >= 0` | Afín | Restricción de desigualdad |

### Maximización del Sharpe (transformación)

El ratio de Sharpe no es directamente convexo. Se usa la **transformación de Cornuejols y Tütüncü**:

Definir y = w / κ y resolver:

$$
\min_{\mathbf{y}, \kappa} \quad \mathbf{y}^\top \boldsymbol{\Sigma} \, \mathbf{y}
$$

sujeto a:

$$
(\boldsymbol{\mu} - r_f)^\top \mathbf{y} = 1, \qquad \sum_i y_i = \kappa, \qquad \mathbf{y} \geq 0, \qquad \kappa \geq 0
$$

Luego los pesos óptimos son w* = y* / κ*.

### Frontera eficiente paramétrica

Se usa `cp.Parameter()` con `warm_start=True` para resolver eficientemente múltiples QPs variando el rendimiento objetivo.

---

## 5. Selección de activos mediante clustering

Cuando el universo de activos es grande, es útil **agrupar** activos similares antes de construir un portafolio.

### K-Means

Agrupa activos en k clusters según su perfil rendimiento-riesgo (media, desviación estándar). Útil para identificar activos con comportamiento similar y seleccionar representantes de cada grupo.

### Clustering jerárquico

El **dendrograma** muestra la estructura de similitud entre activos basada en la correlación (típicamente Spearman). Activos en la misma rama se mueven de forma similar. Se usa la **distancia de correlación**: d = 1 - ρ.

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press.
  - Cap. 4: Convex optimization problems.
- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson.
  - Cap. 22: Estimating Volatilities and Correlations.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
  - Cap. 6–8: Mean-Variance Portfolio Theory.
- **Tsay, R. S.** (2010). *Analysis of Financial Time Series* (3rd ed.). Wiley.
  - Cap. 9: Portfolio Analysis.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

### Artículos seminales

- **Markowitz, H.** (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.
- **Sharpe, W. F.** (1966). Mutual Fund Performance. *The Journal of Business*, 39(1), 119–138.
- **Sharpe, W. F.** (1964). Capital Asset Prices. *The Journal of Finance*, 19(3), 425–442.
- **Cont, R.** (2001). Empirical Properties of Asset Returns. *Quantitative Finance*, 1(2), 223–236.

---

## Recursos adicionales

### Documentación de paquetes

| Paquete | Uso en esta clase |
|---------|-------------------|
| [CVXPY](https://www.cvxpy.org/) | Optimización convexa (DCP) |
| `numpy.cov()` | Matriz de covarianza muestral |
| `sklearn.cluster.KMeans` | Clustering de activos |
| `scipy.cluster.hierarchy` | Dendrograma jerárquico |

### Conexión con otras clases

| Clase | Relación |
|-------|----------|
| **Clase 2** | Covarianza y correlación (insumos para optimización) |
| **Clase 3** | Opciones como instrumentos de cobertura del portafolio |
| **Clase 5** | Mejora la estimación de Σ con Shrunk Covariance |
| **Clase 6** | Mejora la estimación de μ con el estimador de Huber |
| **Clase 11** | Frontera eficiente con CVXPY y funciones reutilizables |

---

## Mapa conceptual de la Clase 4

```
Selección de portafolios
    │
    ├── Rendimiento y riesgo
    │     ├── μ_p = w'μ
    │     ├── σ²_p = w'Σw
    │     └── Restricción: Σwᵢ = 1, wᵢ ≥ 0
    │
    ├── Ratio de Sharpe
    │     ├── S = (μ_p - r_f) / σ_p
    │     ├── Portafolio tangente (max S)
    │     └── Transformación DCP para maximizar S
    │
    ├── Frontera eficiente (Markowitz)
    │     ├── QP paramétrico con CVXPY
    │     ├── cp.quad_form(w, Σ) → convexa
    │     ├── cp.Parameter() + warm_start
    │     └── MVP: mínima varianza global
    │
    └── Selección de activos
          ├── K-Means: perfil rendimiento-riesgo
          └── Jerárquico: dendrograma de correlación
```

---


## Navegación del curso

← **Anterior**: Clase 3: Opciones financieras  
→ **Siguiente**: Clase 5: Covarianza robusta (Shrunk Covariance)

---

*Archivo de apoyo para la Clase 4 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
