# Clase 13 — Portafolio con bono: comparación Monte Carlo vs Markowitz

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/13.%20Clase%2013/13Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F13.%20Clase%2013%2F13Class%20NB.ipynb)

---

## Objetivo

Comparar la simulación Monte Carlo con la optimización de Markowitz para portafolios que incluyen un activo libre de riesgo (bono), usando tres métodos de simulación de rendimientos (normal, histograma, KDE) y clasificando los precios finales en regiones de riesgo.

---

## Contenido teórico

### Tres modelos de simulación de rendimientos

| Modelo | Generación de rendimientos | Captura colas pesadas | Resultado |
|--------|---------------------------|:---------------------:|-----------|
| **Normal** | r ~ N(μ, σ²) con estimadores Huber | No | Base de comparación (supuesto GBM) |
| **Histograma** | Muestreo empírico discreto (250 bins) | Sí | Captura la forma real |
| **KDE** | Kernel gaussiano suavizado | Sí | Continuo y flexible |

### Regiones de riesgo

Dados dos niveles de precio K₁ < K₂, el precio final S_T se clasifica en:

- S_T < K₁ — zona de **pérdida** significativa
- K₁ ≤ S_T ≤ K₂ — zona **neutral**
- S_T > K₂ — zona de **ganancia** significativa

La distribución de frecuencias entre regiones revela las diferencias en colas entre los tres modelos. El modelo normal tiende a **subestimar** las colas, mientras que histograma y KDE capturan mejor los eventos extremos.

### CML como SOCP (Boyd & Vandenberghe, 2004, §4.3.2)

El problema de encontrar el portafolio tangente (máximo Sharpe) es una **programación fraccional**:

$$
\max_{\mathbf{w}} \quad \frac{\boldsymbol{\mu}^\top \mathbf{w} - r_f}{\sqrt{\mathbf{w}^\top \Sigma \mathbf{w}}}
$$

sujeto a:

$$
\sum_i w_i = 1, \qquad w_i \geq 0
$$

Usando la **transformación de Charnes-Cooper** (y = w/κ), se convierte en un SOCP:

$$
\min_{\mathbf{y}, \kappa} \quad \left\| \Sigma^{1/2} \mathbf{y} \right\|_2
$$

sujeto a:

$$
(\boldsymbol{\mu} - r_f)^\top \mathbf{y} = 1, \qquad \sum_i y_i = \kappa, \qquad \mathbf{y} \geq 0
$$

y los pesos se recuperan como w* = y*/κ*. El SOCP es convexo y se resuelve eficientemente con solvers de punto interior.

### Precio sombra del riesgo (Boyd & Vandenberghe, 2004, §5.6)

En el problema donde se maximiza rendimiento sujeto a riesgo máximo, el multiplicador dual λ* de la restricción de riesgo coincide con el **ratio de Sharpe del portafolio tangente**. Esto da una interpretación precisa: el Sharpe mide la tasa marginal de sustitución entre rendimiento y riesgo en el óptimo.

### Monte Carlo vs. Markowitz

| Aspecto | Monte Carlo | Markowitz (CVXPY) |
|---------|------------|-------------------|
| **Resultado** | Nube de portafolios factibles | Frontera eficiente exacta |
| **Óptimo** | Aproximado (mejor de N muestras) | Exacto (solución del QP) |
| **Bono** | Incluido como activo adicional en Dirichlet | Incluido con Σ extendida |
| **Visualización** | Scatter plot coloreado por Sharpe | Curva que envuelve la nube MC |

---

## Recursos adicionales

### Documentación

| Recurso | Descripción |
|---------|-------------|
| [CVXPY](https://www.cvxpy.org/) | Optimización convexa (DCP) |
| [sklearn.neighbors.KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html) | KDE en scikit-learn |
| [numpy.random.dirichlet](https://numpy.org/doc/stable/reference/random/generated/numpy.random.dirichlet.html) | Generación de pesos aleatorios |

### Conexión con otras clases

| Clase | Relación |
|-------|----------|
| **Clase 7** | Tres modelos de simulación (normal, histograma, KDE) |
| **Clase 8** | Valuación MC de opciones con los mismos modelos |
| **Clase 9** | Monte Carlo vs. Markowitz (sin bono) |
| **Clase 10** | CML y activo libre de riesgo |
| **Clase 11** | Frontera eficiente con portfolio_func.py |

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §4.3.2 (SOCP/CML), §5.6 (precios sombra).
- **Glasserman, P.** (2003). *Monte Carlo Methods in Financial Engineering*. Springer.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press. — Cap. 6–8.
- **Markowitz, H.** (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.
- **Sharpe, W. F.** (1964). Capital Asset Prices. *The Journal of Finance*, 19(3), 425–442.
- **Tobin, J.** (1958). Liquidity Preference as Behavior Towards Risk. *The Review of Economic Studies*, 25(2), 65–86.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

---

## Navegación del curso

← **Anterior**: Clase 12: Optimización avanzada
→ **Siguiente**: Clase 14: Opciones barrera

---

*Archivo de apoyo para la Clase 13 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
