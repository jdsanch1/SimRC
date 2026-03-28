# Clase 7 — Comparación de estimadores y análisis de riesgo

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/07.%20Clase%207/07Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F07.%20Clase%207%2F07Class%20NB.ipynb)

---

## Objetivo

Simular trayectorias de precios usando tres modelos de rendimientos (normal, histograma empírico, KDE), comparar estimadores clásicos vs. robustos (Huber), y medir el riesgo mediante **VaR** y **CVaR**.

---

## 1. Simulación Monte Carlo de precios

### Modelo de precios

Bajo el modelo GBM, el precio futuro a T días es:

$$
S_T = S_0 \exp\!\left(\sum_{t=1}^{T} r_t\right)
$$

donde los rendimientos diarios se generan según distintos modelos.

### Tres modelos de simulación

| Modelo | Generación de r_t | Ventaja | Limitación |
|--------|-------------------|---------|------------|
| **Normal** | r ~ N(μ, σ²) | Simple, analítico | Ignora colas pesadas |
| **Histograma** | Muestreo discreto de la distribución empírica | Captura la forma real | Discreto, ruidoso con pocos datos |
| **KDE** | Muestreo de un kernel suavizado | Continuo, captura colas | Sensible al bandwidth |

### Estimación de densidad por kernel (KDE)

La KDE suaviza la distribución empírica:

$$
\hat{f}(r) = \frac{1}{Th}\sum_{t=1}^{T} K\!\left(\frac{r - r_t}{h}\right)
$$

donde K es el kernel (típicamente gaussiano) y h es el **bandwidth** (ancho de banda).

---

## 2. Medidas de riesgo

### Value at Risk (VaR)

El VaR al nivel de confianza α (e.g., 95%) responde: "¿Cuál es la pérdida máxima que no se excede con probabilidad α?"

$$
\text{VaR}_\alpha = -\text{Percentil}_{1-\alpha}(\text{PnL})
$$

**Ejemplo**: VaR₉₅% = 5% significa que hay un 5% de probabilidad de perder más del 5% del valor del portafolio.

### Conditional VaR (CVaR / Expected Shortfall)

El CVaR responde: "Si las cosas van mal (peor que el VaR), ¿cuánto se pierde en promedio?"

$$
\text{CVaR}_\alpha = -\mathbb{E}[\text{PnL} \mid \text{PnL} \leq -\text{VaR}_\alpha]
$$

Minimizar el CVaR de un portafolio se puede formular como un problema de programación cónica de segundo orden (SOCP), lo que lo hace tratable mediante optimización convexa (Boyd & Vandenberghe, 2004, §4.3.2; Rockafellar & Uryasev, 2000).

### Propiedades

| Propiedad | VaR | CVaR |
|-----------|:---:|:----:|
| Fácil de interpretar | Sí | Sí |
| Coherente (Artzner et al., 1999) | No | **Sí** |
| Subaditivo | No siempre | **Siempre** |
| Sensible a la cola | No | **Sí** |

> La **subaditividad** significa que el riesgo de un portafolio es ≤ la suma de los riesgos individuales. El VaR puede violar esta propiedad, lo que lo hace inadecuado como medida regulatoria en algunos contextos. El CVaR siempre la satisface.

### Métodos de estimación del VaR

| Método | Descripción |
|--------|-------------|
| **Paramétrico** | Asume normalidad: VaR = μ - z_α · σ (cotas de Chebyshev permiten relajar este supuesto; Boyd & Vandenberghe, 2004, §6.2) |
| **Histórico** | Percentil de los rendimientos observados |
| **Monte Carlo** | Percentil de las simulaciones (usado en esta clase) |

---

## 3. Comparación de estimadores

### Clásicos vs. robustos

| Parámetro | Clásico | Robusto | Clase |
|-----------|---------|---------|-------|
| Media μ | Media muestral | **Huber** | Clase 6 |
| Covarianza Σ | Muestral | **Ledoit-Wolf** | Clase 5 |

Los estimadores robustos producen:
- Simulaciones más **conservadoras** (menos influenciadas por outliers)
- VaR y CVaR más **estables** ante datos contaminados
- Portafolios óptimos más **diversificados**

---

## 4. Medidas coherentes de riesgo

Artzner et al. (1999) definen cuatro axiomas que una medida de riesgo ρ debe satisfacer para ser **coherente**:

1. **Monotonicidad**: si X ≤ Y, entonces ρ(X) ≥ ρ(Y)
2. **Invarianza por traslación**: ρ(X + c) = ρ(X) - c
3. **Homogeneidad positiva**: ρ(λX) = λρ(X) para λ > 0
4. **Subaditividad**: ρ(X + Y) ≤ ρ(X) + ρ(Y)

El CVaR satisface los cuatro axiomas. El VaR falla en subaditividad para distribuciones no elípticas.

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §4.3.2 (SOCP y CVaR), §6.2 (cotas de Chebyshev para VaR).
- **Glasserman, P.** (2003). *Monte Carlo Methods in Financial Engineering*. Springer. — Cap. 1–3.
- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson. — Cap. 22: Value at Risk.
- **McNeil, A. J., Frey, R. & Embrechts, P.** (2015). *Quantitative Risk Management* (2nd ed.). Princeton University Press. — Cap. 2: Basic Concepts in Risk Management.
- **Tsay, R. S.** (2010). *Analysis of Financial Time Series* (3rd ed.). Wiley. — Cap. 7: Value at Risk.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

### Artículos seminales

- **Artzner, P., Delbaen, F., Eber, J.-M. & Heath, D.** (1999). Coherent Measures of Risk. *Mathematical Finance*, 9(3), 203–228.
- **Cont, R.** (2001). Empirical Properties of Asset Returns. *Quantitative Finance*, 1(2), 223–236.
- **Huber, P. J.** (1964). Robust Estimation of a Location Parameter. *The Annals of Mathematical Statistics*, 35(1), 73–101.
- **Ledoit, O. & Wolf, M.** (2004). A well-conditioned estimator for large-dimensional covariance matrices. *Journal of Multivariate Analysis*, 88(2), 365–411.

---

## Recursos adicionales

### Documentación

| Recurso | Descripción |
|---------|-------------|
| [sklearn.neighbors.KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html) | KDE en scikit-learn |
| [statsmodels.robust.scale.Huber](https://www.statsmodels.org/stable/generated/statsmodels.robust.scale.Huber.html) | Estimador de Huber |
| [numpy.random.normal](https://numpy.org/doc/stable/reference/random/generated/numpy.random.normal.html) | Generación de normales |

### Conexión con otras clases

| Clase | Relación |
|-------|----------|
| **Clase 5** | Covarianza robusta (Ledoit-Wolf) |
| **Clase 6** | Media robusta (Huber) + generación de números aleatorios |
| **Clase 8** | Resumen y consolidación de funciones |
| **Clase 9** | Monte Carlo refinado para portafolios completos |
| **Clase 14** | Opciones barrera simuladas con Monte Carlo |

---

## Mapa conceptual de la Clase 7

```
Datos históricos (rendimientos)
    │
    ├── Modelo Normal: r ~ N(μ, σ²)
    ├── Modelo Histograma: muestreo empírico
    └── Modelo KDE: suavizado por kernel
            │
            └── Simulación Monte Carlo
                    │
                    ├── Trayectorias de precios: S_T = S₀·exp(Σ rₜ)
                    │
                    ├── Distribución de precios finales
                    │
                    ├── Medidas de riesgo
                    │     ├── VaR: percentil de las pérdidas
                    │     └── CVaR: pérdida esperada en la cola
                    │
                    └── Comparación de estimadores
                          ├── Clásico (media + std muestral)
                          └── Robusto (Huber μ + Huber σ)
```

---


## Navegación del curso

← **Anterior**: Clase 6: Media robusta y RNG  
→ **Siguiente**: Clase 8: Resumen Parte 1

---

*Archivo de apoyo para la Clase 7 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
