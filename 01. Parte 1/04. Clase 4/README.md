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

**Definición (Cuasi-convexidad, Boyd §3.4).** Una función $f: \mathbb{R}^n \to \mathbb{R}$ es **cuasi-convexa** si sus conjuntos de subnivel $S_\alpha = \{x \mid f(x) \leq \alpha\}$ son convexos para todo $\alpha$. Es **cuasi-cóncava** si $-f$ es cuasi-convexa, equivalentemente si los conjuntos de supernivel $\{x \mid f(x) \geq \alpha\}$ son convexos.

El ratio de Sharpe $S(\mathbf{w}) = \frac{\boldsymbol{\mu}^\top\mathbf{w} - r_f}{\sqrt{\mathbf{w}^\top\boldsymbol{\Sigma}\,\mathbf{w}}}$ es **cuasi-cóncavo** en $\mathbf{w}$ (para $\boldsymbol{\mu}^\top\mathbf{w} > r_f$): es el cociente de una función afín (cóncava) y una convexa positiva ($\sigma_p$). Los conjuntos de supernivel $\{w \mid S(w) \geq \alpha\}$ son convexos (intersección de un semiplano afín y una restricción cónica), lo que garantiza que el máximo global es único.

**Transformación de Charnes-Cooper (Boyd §4.3.2).** Como $S(\mathbf{w})$ es cuasi-cóncavo pero no cóncavo, no se puede maximizar directamente con DCP. La transformación consiste en el cambio de variable $\mathbf{y} = \mathbf{w}/\kappa$ donde $\kappa = 1/(\boldsymbol{\mu}^\top\mathbf{w} - r_f) > 0$. El problema equivalente es:

$$
\min_{\mathbf{y},\kappa} \; \mathbf{y}^\top\boldsymbol{\Sigma}\,\mathbf{y} \quad \text{s.a.} \quad (\boldsymbol{\mu} - r_f\mathbf{1})^\top\mathbf{y} = 1, \; \mathbf{1}^\top\mathbf{y} = \kappa, \; \mathbf{y} \geq 0, \; \kappa > 0
$$

y los pesos óptimos se recuperan como $\mathbf{w}^* = \mathbf{y}^*/\kappa^*$. Este es un QP convexo estándar.

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

Este es un **problema cuadrático convexo** (QP).

**Definición (Programa cuadrático, Boyd §4.4).** Un QP tiene la forma estándar:

$$
\min_{\mathbf{x}} \; \frac{1}{2}\mathbf{x}^\top P\,\mathbf{x} + \mathbf{q}^\top\mathbf{x} \quad \text{s.a.} \quad G\mathbf{x} \leq \mathbf{h}, \; A\mathbf{x} = \mathbf{b}
$$

con $P \succeq 0$. Para el problema de Markowitz:

| Elemento QP | Correspondencia Markowitz |
|---|---|
| $\mathbf{x}$ | Vector de pesos $\mathbf{w}$ |
| $P$ | $2\boldsymbol{\Sigma}$ (matriz de covarianza) |
| $\mathbf{q}$ | $\mathbf{0}$ (sin término lineal en el objetivo) |
| $G$ | $-\mathbf{I}_n$ (restricciones $w_i \geq 0$) |
| $\mathbf{h}$ | $\mathbf{0}$ |
| A | Matriz de restricciones de igualdad (rendimiento objetivo + pesos suman 1) |
| b | Vector objetivo (μ*, 1) |

**Reglas de verificación DCP (Boyd §3.2).** CVXPY valida convexidad mediante reglas composicionales:

| Regla | Ejemplo en Markowitz |
|---|---|
| Suma de convexas es convexa | $\mathbf{w}^\top\boldsymbol{\Sigma}\,\mathbf{w}$ es convexa (forma cuadrática con $\boldsymbol{\Sigma} \succeq 0$) |
| Función afín es convexa y cóncava | $\boldsymbol{\mu}^\top\mathbf{w}$, $\sum w_i$ |
| Restricción afín = 0 es válida | $\boldsymbol{\mu}^\top\mathbf{w} = \mu^*$ |
| Restricción afín $\leq$ 0 es válida | $-w_i \leq 0$ |

El QP tiene solución global única cuando $\boldsymbol{\Sigma} \succ 0$.

**Teorema (Optimización paramétrica, Boyd §5.6.1).** Sea $p^*(\mu^*)$ la función de valor óptimo del QP de Markowitz parametrizada por el rendimiento objetivo $\mu^*$. Entonces $p^*(\mu^*)$ es convexa en $\mu^*$.

*Prueba (esquema).* El conjunto factible se contrae cuando se impone una restricción más estricta sobre $\mu^*$. Formalmente, $p^*(\mu^*) = \inf_{\mathbf{w} \in \mathcal{F}(\mu^*)} \mathbf{w}^\top\boldsymbol{\Sigma}\,\mathbf{w}$ donde $\mathcal{F}(\mu^*) = \{\mathbf{w} \mid \boldsymbol{\mu}^\top\mathbf{w} = \mu^*, \sum w_i = 1, w_i \geq 0\}$. Para $\theta \in [0,1]$, los portafolios factibles para $\theta\mu_1^* + (1-\theta)\mu_2^*$ contienen las combinaciones convexas de los factibles para $\mu_1^*$ y $\mu_2^*$, y por convexidad de la forma cuadrática se obtiene $p^*(\theta\mu_1^*+(1-\theta)\mu_2^*) \leq \theta p^*(\mu_1^*) + (1-\theta) p^*(\mu_2^*)$. ∎

*Interpretación financiera*: la frontera eficiente en el espacio $(\sigma_p^2, \mu_p)$ es una curva convexa. Esto garantiza suavidad y continuidad: no hay "saltos" en la frontera, y el tradeoff riesgo-rendimiento se encarece de forma creciente.

### Portafolio de mínima varianza (MVP)

El punto más a la izquierda de la frontera es el **portafolio de mínima varianza global**:

$$
\min_{\mathbf{w}} \quad \mathbf{w}^\top \boldsymbol{\Sigma} \, \mathbf{w} \qquad \text{s.a.} \quad \sum_i w_i = 1, \quad w_i \geq 0
$$

---

## 4. Optimización con CVXPY (DCP)

### Programación Convexa Disciplinada

CVXPY utiliza el paradigma **DCP** (Disciplined Convex Programming, Boyd & Vandenberghe, 2004, §4.2.3) para verificar automáticamente la convexidad:

| Expresión CVXPY | Tipo DCP | Válida en |
|---|---|---|
| `cp.quad_form(w, Σ)` | Convexa | Objetivo (minimizar) |
| `μ @ w` | Afín | Objetivo o restricción |
| `cp.sum(w) == 1` | Afín | Restricción de igualdad |
| `w >= 0` | Afín | Restricción de desigualdad |

### Maximización del Sharpe (transformación)

El ratio de Sharpe es una función **cuasi-convexa** — razón de una función afín y una convexa (Boyd & Vandenberghe, 2004, §4.3.2). Se usa la **transformación de Cornuejols y Tütüncü** para convertirlo en un QP estándar:

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

Se usa `cp.Parameter()` con `warm_start=True` para resolver eficientemente múltiples QPs variando el rendimiento objetivo. El tradeoff rendimiento-riesgo es un problema bi-criterio cuya frontera eficiente coincide con el **conjunto de Pareto** (Boyd & Vandenberghe, 2004, §4.7.4).

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

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — Cap. 4 (§4.2.3 DCP, §4.3.2 funciones cuasi-convexas, §4.4 QP, §4.7.3–4.7.4 optimización paramétrica y multi-criterio).
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
