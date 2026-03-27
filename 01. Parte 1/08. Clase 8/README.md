# Clase 8 — Resumen Parte 1: Valuación de opciones por simulación Monte Carlo

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/08.%20Clase%208/08Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F08.%20Clase%208%2F08Class%20NB.ipynb)

---

## Objetivo

Consolidar los conceptos de la Parte 1 del curso aplicándolos a la **valuación de opciones europeas por simulación Monte Carlo**. Se comparan tres modelos de simulación de rendimientos y se analiza la convergencia del estimador.

---

## 1. Valuación de opciones por Monte Carlo

### Fundamento teórico

El precio de una opción europea es el valor esperado descontado de su payoff bajo la medida de riesgo neutro Q:

**Call:**

$$
C_0 = e^{-rT} \, \mathbb{E}^{\mathbb{Q}}[\max(S_T - K, 0)]
$$

**Put:**

$$
P_0 = e^{-rT} \, \mathbb{E}^{\mathbb{Q}}[\max(K - S_T, 0)]
$$

### Aproximación Monte Carlo

Se generan N trayectorias independientes del precio final y se promedia:

$$
\hat{C}_0 = e^{-rT} \frac{1}{N} \sum_{i=1}^{N} \max(S_T^{(i)} - K, 0)
$$

Este método fue propuesto por Boyle (1977) y es el enfoque estándar para opciones con payoffs complejos donde no existe solución analítica.

### Drift risk-neutral

Para simular bajo la medida Q, el drift del GBM se reemplaza por la tasa libre de riesgo:

$$
r_t \sim \mathcal{N}\!\left(r_f - \frac{\sigma^2}{2}, \; \sigma^2\right)
$$

donde r_f es la tasa libre de riesgo diaria y σ es la volatilidad estimada de los rendimientos históricos.

---

## 2. Tres modelos de simulación

| Modelo | Genera r_t mediante | Captura colas pesadas | Continuo |
|--------|---------------------|:---------------------:|:--------:|
| **Normal** | N(μ, σ²) | No | Sí |
| **Histograma** | Muestreo empírico discreto | Sí | No |
| **KDE** | Kernel suavizado | Sí | Sí |

### Modelo Normal

Asume log-normalidad (supuesto del modelo Black-Scholes). Es simple y permite comparación con la fórmula analítica, pero ignora los hechos estilizados (colas pesadas, asimetría).

### Modelo Histograma

Construye una distribución discreta a partir de los rendimientos observados y muestrea con reemplazo. Captura la forma real pero es ruidoso con pocos datos.

### Modelo KDE

Suaviza la distribución empírica con un kernel gaussiano. Produce muestras continuas que preservan las características reales (colas, asimetría) sin el ruido del histograma.

---

## 3. Convergencia Monte Carlo

### Error estándar

El error de la estimación MC decrece como la raíz inversa de N:

$$
\text{SE} = \frac{\hat{\sigma}_{\text{payoff}}}{\sqrt{N}}
$$

| N trayectorias | Error relativo |
|:--------------:|:--------------:|
| 100 | ~10% |
| 1,000 | ~3% |
| 10,000 | ~1% |
| 100,000 | ~0.3% |

### Intervalo de confianza

Un intervalo de confianza al 95% para el precio es:

$$
\hat{C}_0 \pm 1.96 \cdot \text{SE}
$$

### Técnicas de reducción de varianza

Para mejorar la convergencia (no cubiertas en esta clase):
- **Variables antitéticas**: usar -Z además de Z para cada normal
- **Variables de control**: usar la solución de Black-Scholes como control
- **Muestreo estratificado**: dividir el espacio de probabilidad en estratos

---

## 4. Evolución temporal del precio de la opción

El precio de la opción cambia con el **tiempo al vencimiento** τ = T - t. A medida que τ → 0:
- El **valor temporal** (time value) disminuye (theta decay)
- La opción converge a su **valor intrínseco**: max(S_t - K, 0) para calls

Esto se visualiza calculando el precio MC para cada horizonte intermedio t = 1, ..., T.

---

## 5. Resumen de la Parte 1

| Clase | Tema | Herramienta clave |
|-------|------|-------------------|
| 1 | Análisis de acciones | yfinance, rendimientos log, volatilidad |
| 2 | Retornos y covarianza | Matriz Σ, correlación |
| 3 | Opciones financieras | Payoff, P&L, IV, paridad put-call |
| 4 | Portafolio óptimo | Sharpe, frontera eficiente, CVXPY |
| 5 | Covarianza robusta | ShrunkCovariance, LedoitWolf |
| 6 | Media robusta + RNG | Huber, LCG, Box-Muller |
| 7 | Simulación de riesgo | Monte Carlo, VaR, CVaR |
| **8** | **Valuación MC** | **Normal, histograma, KDE** |

### Flujo completo de la Parte 1

```
Datos (yfinance)
  → Rendimientos logarítmicos
    → Estimadores (μ: Huber, Σ: Ledoit-Wolf)
      → Simulación Monte Carlo
        → Portafolios óptimos (CVXPY)
        → Valuación de opciones
        → Medidas de riesgo (VaR, CVaR)
```

---

## Referencias bibliográficas

### Textos principales

- **Glasserman, P.** (2003). *Monte Carlo Methods in Financial Engineering*. Springer. — Cap. 1–4.
- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson. — Cap. 15, 22.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
- **McNeil, A. J., Frey, R. & Embrechts, P.** (2015). *Quantitative Risk Management* (2nd ed.). Princeton University Press.
- **Tsay, R. S.** (2010). *Analysis of Financial Time Series* (3rd ed.). Wiley.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning. — Cap. 7: Simulación Monte Carlo.

### Artículos seminales

- **Black, F. & Scholes, M.** (1973). The Pricing of Options and Corporate Liabilities. *Journal of Political Economy*, 81(3), 637–654.
- **Boyle, P. P.** (1977). Options: A Monte Carlo Approach. *Journal of Financial Economics*, 4(3), 323–338.
- **Cont, R.** (2001). Empirical Properties of Asset Returns. *Quantitative Finance*, 1(2), 223–236.
- **Ledoit, O. & Wolf, M.** (2004). A well-conditioned estimator for large-dimensional covariance matrices. *Journal of Multivariate Analysis*, 88(2), 365–411.

---

## Recursos adicionales

### Documentación

| Recurso | Descripción |
|---------|-------------|
| [numpy.random](https://numpy.org/doc/stable/reference/random/) | Generadores de números aleatorios de NumPy |
| [sklearn.neighbors.KernelDensity](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KernelDensity.html) | KDE en scikit-learn |
| [scipy.stats](https://docs.scipy.org/doc/scipy/reference/stats.html) | Distribuciones y tests estadísticos |

### Conexión con la Parte 2

| Clase | Tema | Relación con Parte 1 |
|-------|------|---------------------|
| 9 | MC refinado para portafolios | Extiende simulación MC a portafolios completos |
| 10 | Activo libre de riesgo | Agrega bonos al portafolio optimizado |
| 11 | Frontera eficiente con CVXPY | Usa portfolio_func.py con Huber + Shrunk |
| 14 | Opciones barrera | Extiende valuación MC a opciones exóticas |
| 15 | Programación estocástica | Pyomo para problemas con incertidumbre |

---

## Mapa conceptual de la Clase 8

```
Valuación de opciones por Monte Carlo
    │
    ├── Fundamento: C₀ = e^(-rT) · E^Q[max(S_T - K, 0)]
    │
    ├── Tres modelos de simulación
    │     ├── Normal: r ~ N(μ, σ²)
    │     ├── Histograma: muestreo empírico
    │     └── KDE: kernel suavizado
    │
    ├── Drift risk-neutral: r_f - σ²/2
    │
    ├── Convergencia
    │     ├── SE = σ_payoff / √N
    │     └── IC 95%: Ĉ ± 1.96·SE
    │
    ├── Evolución temporal (theta decay)
    │
    └── Consolidación Parte 1
          ├── Datos → Rendimientos → Estimadores robustos
          └── → Simulación MC → Valuación / Riesgo
```

---


## Navegación del curso

← **Anterior**: Clase 7: Comparación de estimadores  
→ **Siguiente**: Parte 2: Optimización y Productos Derivados

---

*Archivo de apoyo para la Clase 8 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
