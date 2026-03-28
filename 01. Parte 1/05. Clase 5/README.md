# Clase 5 — Covarianza robusta (Shrunk Covariance)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/05.%20Clase%205/05Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F05.%20Clase%205%2F05Class%20NB.ipynb)

---

## Objetivo

Introducir los **estimadores de contracción** (shrinkage) para la matriz de covarianza como alternativa robusta a la estimación muestral. Comparar el impacto en la optimización de portafolios y la estabilidad de los pesos óptimos.

---

## 1. El problema de la covarianza muestral

### Maldición de la dimensionalidad

La covarianza muestral de n activos tiene n(n+1)/2 parámetros libres:

| n activos | Parámetros | Con T = 250 días |
|:---------:|:----------:|:-----------------:|
| 10 | 55 | Bien condicionado |
| 50 | 1,275 | Inestable |
| 100 | 5,050 | Muy inestable |
| 500 | 125,250 | Singular si T < n |

Cuando n se acerca a T (o lo supera), la covarianza muestral se vuelve **singular** o **mal condicionada** (Ledoit & Wolf, 2004).

### Consecuencias para portafolios

La optimización de Markowitz es extremadamente sensible a errores de estimación en Σ:

1. **Pesos extremos**: el optimizador "explota" covarianzas ruidosas, generando posiciones grandes
2. **Inestabilidad temporal**: pequeños cambios en los datos producen pesos completamente diferentes
3. **Sobreajuste**: el portafolio "óptimo" en muestra tiene mal desempeño fuera de muestra

> "Mean-variance optimization is, in practice, estimation-error maximization" — Michaud (1989)

---

## 2. Estimadores de contracción (Shrinkage)

### Idea fundamental

Combinar la covarianza muestral (mucho ruido, poco sesgo) con una **matriz objetivo** más estable (poco ruido, más sesgo). Este promedio convexo es una forma de regularización (Boyd & Vandenberghe, 2004, §6.3–6.4) que mejora la estabilidad numérica:

$$
\hat{\boldsymbol{\Sigma}}_{\text{shrunk}} = (1 - \alpha) \, \hat{\boldsymbol{\Sigma}} + \alpha \, \mathbf{F}
$$

Donde:
- La covarianza muestral captura toda la estructura pero con mucho ruido
- F es la **matriz objetivo** (target), típicamente diagonal
- α es el **coeficiente de contracción** que balancea sesgo y varianza

**Proposición (Shrinkage como regularización convexa, Boyd §6.3).** El estimador de contracción es la solución de un problema de optimización convexa regularizado. En el marco general de Boyd & Vandenberghe (2004, §6.3), un estimador regularizado minimiza:

$$
\hat{\theta} = \arg\min_{\theta} \; \ell(\theta) + \gamma \, R(\theta)
$$

donde $\ell(\theta)$ es la pérdida (ajuste a los datos) y $R(\theta)$ es el regularizador (penalización por complejidad). Los tres casos principales son:

| Regularizador $R(\theta)$ | Nombre | Efecto | Ejemplo financiero |
|---|---|---|---|
| $\|\theta\|_2^2$ (norma $L_2$ al cuadrado) | Ridge / Tikhonov | Contrae parámetros hacia cero | Shrinkage hacia $\mathbf{F} = \frac{\text{tr}(\hat{\Sigma})}{n}\mathbf{I}$ |
| $\|\theta\|_1$ (norma $L_1$) | LASSO | Produce soluciones **dispersas** (sparsity) | Selección de activos (covarianza sparse) |
| $\|\theta - \theta_0\|_F^2$ (distancia a un objetivo) | Contracción hacia target | Contrae hacia una estructura previa $\theta_0$ | $\hat{\Sigma}_{\text{shrunk}}$ hacia $\text{diag}(\hat{\Sigma})$ |

*Prueba de que el shrinkage resuelve una proyección convexa regularizada.* El estimador de Ledoit-Wolf minimiza la pérdida cuadrática $\|\hat{\Sigma}_{\text{shrunk}} - \Sigma\|_F^2$ sobre combinaciones convexas de $\hat{\Sigma}$ y $\mathbf{F}$. Sustituyendo $\hat{\Sigma}_{\text{shrunk}} = (1-\alpha)\hat{\Sigma} + \alpha\mathbf{F}$ y derivando respecto a $\alpha$, el problema se reduce a una minimización cuadrática univariada en $\alpha \in [0,1]$, que es convexa con solución cerrada. El conjunto factible $\{(1-\alpha)\hat{\Sigma} + \alpha\mathbf{F} \mid \alpha \in [0,1]\}$ es un segmento de línea en el espacio de matrices (convexo), y la función objetivo es cuadrática convexa en $\alpha$. $\blacksquare$

*Interpretación financiera*: al agregar regularización, aceptamos un pequeño sesgo a cambio de una reducción significativa en la varianza del estimador. El parámetro $\gamma$ (o $\alpha$) controla este tradeoff sesgo-varianza, que es análogo al tradeoff rendimiento-riesgo en la teoría de portafolios.

### Elección de la matriz objetivo

**Opción 1: Identidad escalada**

$$
\mathbf{F} = \frac{\text{tr}(\hat{\boldsymbol{\Sigma}})}{n} \cdot \mathbf{I}_n
$$

Asume que todos los activos tienen la misma varianza y covarianza cero. Es la opción por defecto en `sklearn.covariance.ShrunkCovariance`.

**Opción 2: Diagonal de la muestral**

$$
\mathbf{F} = \text{diag}(\hat{\boldsymbol{\Sigma}})
$$

Preserva las varianzas individuales pero elimina todas las covarianzas.

### Coeficiente óptimo de contracción

Ledoit & Wolf (2004) derivan una fórmula analítica para el α óptimo que minimiza la pérdida cuadrática esperada. Desde la perspectiva de estimación bayesiana, esto equivale a una estimación MAP con un prior que actúa como regularización (Boyd & Vandenberghe, 2004, §7.1–7.2):

$$
\alpha^* = \arg\min_\alpha \, \mathbb{E}\left[\left\| \hat{\boldsymbol{\Sigma}}_{\text{shrunk}}(\alpha) - \boldsymbol{\Sigma} \right\|_F^2\right]
$$

donde la norma de Frobenius mide la distancia matricial. La solución tiene forma cerrada y se implementa en `sklearn.covariance.LedoitWolf`.

---

## 3. Implementación en Python (sklearn)

### Estimadores disponibles

| Clase sklearn | Descripción | α |
|---|---|---|
| `EmpiricalCovariance` | Covarianza muestral (sin contracción) | α = 0 |
| `ShrunkCovariance(shrinkage=α)` | Contracción con α fijo | Elegido por el usuario |
| `LedoitWolf` | Contracción con α óptimo (Ledoit-Wolf) | Estimado automáticamente |
| `OAS` | Oracle Approximating Shrinkage | Estimado automáticamente |

### Ejemplo de uso

```python
from sklearn.covariance import LedoitWolf

lw = LedoitWolf().fit(returns)
print(f"α óptimo: {lw.shrinkage_:.4f}")
Sigma_robust = lw.covariance_
```

---

## 4. Efecto de la contracción

### En las covarianzas

La contracción reduce las covarianzas off-diagonal (fuera de la diagonal) más que las varianzas (diagonal), moderando las relaciones extremas entre activos.

### En los eigenvalores

La contracción **comprime** la distribución de eigenvalores:
- Los eigenvalores más **grandes** se reducen
- Los eigenvalores más **pequeños** aumentan

Esto mejora el **número de condición** de la matriz:

$$
\kappa(\boldsymbol{\Sigma}) = \frac{\lambda_{\max}}{\lambda_{\min}}
$$

Un número de condición menor indica una matriz más estable numéricamente.

### En la frontera eficiente

La frontera eficiente con covarianza contraída es más **conservadora** (se desplaza hacia la derecha): reconoce que hay más incertidumbre en las estimaciones y no promete rendimientos que dependen de correlaciones ruidosas.

### En los pesos óptimos

Los pesos obtenidos con Ledoit-Wolf son más **diversificados** y **estables** que los de la covarianza muestral. Esto se traduce en menor rotación (turnover) y menores costos de transacción.

---

## 5. Selección de activos

Antes de optimizar, es útil reducir el universo de activos agrupando los similares:

### K-Means

Agrupa activos en k clusters según su perfil rendimiento-riesgo. Seleccionar un representante de cada cluster mejora la diversificación.

### Clustering jerárquico

Usa la distancia de correlación d = 1 - ρ para construir un dendrograma. Activos en la misma rama son candidatos a ser redundantes; se puede elegir uno de cada rama.

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §6.3–6.4 (regularización y shrinkage), §7.1–7.2 (estimación ML/MAP de covarianza).
- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson. — Cap. 22.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press. — Cap. 6–8.
- **Tsay, R. S.** (2010). *Analysis of Financial Time Series* (3rd ed.). Wiley.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

### Artículos clave

- **Ledoit, O. & Wolf, M.** (2004). A well-conditioned estimator for large-dimensional covariance matrices. *Journal of Multivariate Analysis*, 88(2), 365–411.
- **Ledoit, O. & Wolf, M.** (2004). Honey, I shrunk the sample covariance matrix. *The Journal of Portfolio Management*, 30(4), 110–119.
- **Markowitz, H.** (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.
- **Michaud, R. O.** (1989). The Markowitz Optimization Enigma: Is 'Optimized' Optimal? *Financial Analysts Journal*, 45(1), 31–42.

---

## Recursos adicionales

### Documentación

| Recurso | Descripción |
|---------|-------------|
| [sklearn.covariance](https://scikit-learn.org/stable/modules/covariance.html) | Documentación oficial de estimadores de covarianza |
| [LedoitWolf API](https://scikit-learn.org/stable/modules/generated/sklearn.covariance.LedoitWolf.html) | Parámetros y ejemplos |
| [CVXPY](https://www.cvxpy.org/) | Optimización convexa (DCP) |

### Conexión con otras clases

| Clase | Relación |
|-------|----------|
| **Clase 2** | Covarianza muestral (sin contracción) |
| **Clase 4** | Optimización de portafolios con covarianza muestral |
| **Clase 6** | Estimador robusto de la **media** (Huber) |
| **Clase 11** | Frontera eficiente con estimadores robustos (Σ shrunk + μ Huber) |

---

## Mapa conceptual de la Clase 5

```
Covarianza muestral (Clase 2-4)
    │
    └── Problemas: inestabilidad, pesos extremos, sobreajuste
            │
            └── Solución: Shrinkage (contracción)
                    │
                    ├── Σ_shrunk = (1-α)·Σ_sample + α·F
                    │     ├── F = identidad escalada
                    │     └── F = diagonal de Σ_sample
                    │
                    ├── Coeficiente α
                    │     ├── Fijo (ShrunkCovariance)
                    │     └── Óptimo (LedoitWolf)
                    │
                    ├── Efectos
                    │     ├── Eigenvalores comprimidos
                    │     ├── Mejor número de condición
                    │     ├── Frontera más conservadora
                    │     └── Pesos más diversificados
                    │
                    └── → Clase 6: estimador robusto de μ (Huber)
```

---


## Navegación del curso

← **Anterior**: Clase 4: Ratio de Sharpe  
→ **Siguiente**: Clase 6: Media robusta (Huber)

---

*Archivo de apoyo para la Clase 5 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
