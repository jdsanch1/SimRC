# Simulación de Riesgos y Coberturas

**[Juan Diego Sánchez Torres](https://www.researchgate.net/profile/Juan_Diego_Sanchez_Torres)**
Profesor — [MAF ITESO](http://maf.iteso.mx/web/general/detalle?group_id=5858156)
dsanchez@iteso.mx

---

## Presentación del curso

Este curso cubre los fundamentos cuantitativos de la **gestión de riesgos financieros** y la **construcción de portafolios**, desde la descarga de datos de mercado hasta la optimización convexa y la valuación de derivados por simulación.

### Enfoque pedagógico

El curso integra tres pilares de forma progresiva:

1. **Teoría financiera** — Rendimientos, volatilidad, opciones (Black-Scholes), frontera eficiente de Markowitz, Capital Market Line, medidas de riesgo (VaR, CVaR), opciones barrera.
2. **Optimización convexa** — Programación cuadrática (QP), cónica (SOCP), convexa disciplinada (DCP), dualidad, condiciones KKT, regularización, optimización robusta. Basado en Boyd & Vandenberghe (2004).
3. **Implementación en Python** — Cada concepto teórico se acompaña de código ejecutable con datos reales de mercado, gráficos interactivos y comparaciones numéricas.

### Cada clase incluye

- **Notebook** (`.ipynb`) — Código ejecutable en Google Colab o Binder con datos de 2025.
- **Lectura teórica** (`README.md`) — Definiciones formales, teoremas con pruebas, ejemplos financieros y referencias bibliográficas.

### Herramientas

| Paquete | Descripción | Clases |
|---------|-------------|:------:|
| [CVXPY](https://www.cvxpy.org/) | Optimización convexa con verificación DCP | 4, 5, 9–13, 15 |
| [Pyomo](https://www.pyomo.org/) | Programación matemática general (MILP) | 15 |
| [yfinance](https://github.com/ranaroussi/yfinance) | Descarga de datos de Yahoo Finance | 1–15 |
| [scikit-learn](https://scikit-learn.org/) | Estimadores robustos (Ledoit-Wolf, KDE, K-Means) | 5, 7, 9–13 |
| [statsmodels](https://www.statsmodels.org/) | Estimador de Huber para media robusta | 6, 9–13 |

### Ejecución en la nube

Todos los notebooks se ejecutan directamente en **Google Colab** o **Binder** (JupyterLab, sin cuenta Google) usando los botones de las tablas de abajo. No requiere instalación local.

---

## Parte 1 — Portafolios, estimación robusta y simulación Monte Carlo

| Clase | Tema | Notebook | Lectura |
|:-----:|------|:--------:|:-------:|
| 1 | Análisis de acciones con Python | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/01.%20Clase%201/01Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F01.%20Clase%201%2F01Class%20NB.ipynb) | [README](01.%20Parte%201/01.%20Clase%201/) |
| 2 | Retornos logarítmicos y matriz de covarianza | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/02.%20Clase%202/02Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F02.%20Clase%202%2F02Class%20NB.ipynb) | [README](01.%20Parte%201/02.%20Clase%202/) |
| 3 | Opciones financieras: payoff, P&L, volatilidad implícita | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/03.%20Clase%203/03Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F03.%20Clase%203%2F03Class%20NB.ipynb) | [README](01.%20Parte%201/03.%20Clase%203/) |
| 4 | Ratio de Sharpe y portafolio óptimo (CVXPY / DCP) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/04.%20Clase%204/04Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F04.%20Clase%204%2F04Class%20NB.ipynb) | [README](01.%20Parte%201/04.%20Clase%204/) |
| 5 | Covarianza robusta (Shrunk Covariance / Ledoit-Wolf) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/05.%20Clase%205/05Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F05.%20Clase%205%2F05Class%20NB.ipynb) | [README](01.%20Parte%201/05.%20Clase%205/) |
| 6 | Media robusta (Huber) y generación de números aleatorios | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/06.%20Clase%206/06Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F06.%20Clase%206%2F06Class%20NB.ipynb) | [README](01.%20Parte%201/06.%20Clase%206/) |
| 7 | Simulación de riesgo: VaR y CVaR | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/07.%20Clase%207/07Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F07.%20Clase%207%2F07Class%20NB.ipynb) | [README](01.%20Parte%201/07.%20Clase%207/) |
| 8 | Resumen Parte 1 — Valuación de opciones por Monte Carlo | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/08.%20Clase%208/08Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F08.%20Clase%208%2F08Class%20NB.ipynb) | [README](01.%20Parte%201/08.%20Clase%208/) |

## Parte 2 — Optimización avanzada y productos derivados

| Clase | Tema | Notebook | Lectura |
|:-----:|------|:--------:|:-------:|
| 9 | Monte Carlo vs. Markowitz (CVXPY) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/09.%20Clase%209/09Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F09.%20Clase%209%2F09Class%20NB.ipynb) | [README](02.%20Parte%202/09.%20Clase%209/) |
| 10 | Activo libre de riesgo y Capital Market Line | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/10.%20Clase%2010/10Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F10.%20Clase%2010%2F10Class%20NB.ipynb) | [README](02.%20Parte%202/10.%20Clase%2010/) |
| 11 | Frontera eficiente con funciones reutilizables (CVXPY) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/11.%20Clase%2011/11Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F11.%20Clase%2011%2F11Class%20NB.ipynb) | [README](02.%20Parte%202/11.%20Clase%2011/) |
| 12 | Regularización de portafolios y estrategias de opciones | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/12.%20Clase%2012/12Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F12.%20Clase%2012%2F12Class%20NB.ipynb) | [README](02.%20Parte%202/12.%20Clase%2012/) |
| 13 | Portafolio con bono — Monte Carlo vs Markowitz | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/13.%20Clase%2013/13Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F13.%20Clase%2013%2F13Class%20NB.ipynb) | [README](02.%20Parte%202/13.%20Clase%2013/) |
| 14 | Opciones barrera (knock-in / knock-out) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/14.%20Clase%2014/14Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F14.%20Clase%2014%2F14Class%20NB.ipynb) | [README](02.%20Parte%202/14.%20Clase%2014/) |
| 15 | Optimización robusta (CVXPY) y programación estocástica (Pyomo) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/15.%20Clase%2015/13Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F15.%20Clase%2015%2F13Class%20NB.ipynb) | [README](02.%20Parte%202/15.%20Clase%2015/) |

---

## Mapa del curso

```
Parte 1: Fundamentos
  Clase 1  Datos, rendimientos, volatilidad, distribuciones
  Clase 2  Covarianza, correlación, beta (CAPM)
  Clase 3  Opciones: payoff, P&L, Black-Scholes, volatilidad implícita
  Clase 4  Frontera eficiente, Sharpe, CVXPY (DCP), Charnes-Cooper
  Clase 5  Covarianza robusta: Shrunk Covariance, Ledoit-Wolf
  Clase 6  Media robusta: Huber, LCG, Box-Muller
  Clase 7  Simulación MC, VaR, CVaR (Expected Shortfall)
  Clase 8  Valuación MC de opciones (normal, histograma, KDE)

Parte 2: Optimización avanzada
  Clase 9  Monte Carlo vs. Markowitz con estimadores robustos
  Clase 10 Capital Market Line, activo libre de riesgo, Tobin
  Clase 11 Frontera eficiente con portfolio_func.py (Huber + LW)
  Clase 12 Regularización L₂/L₁, tracking error (SOCP), estrategias
  Clase 13 Portafolio con bono: MC vs Markowitz, regiones de riesgo
  Clase 14 Opciones barrera (knock-in/out), path-dependent
  Clase 15 QCQP, optimización robusta (SOCP), Pyomo (MILP)
```

### Flujo de conceptos

```
Datos (yfinance)
  → Rendimientos logarítmicos
    → Estimadores robustos
    │   ├── μ: Huber (Clase 6)
    │   └── Σ: Ledoit-Wolf (Clase 5)
    │
    → Simulación Monte Carlo
    │   ├── Portafolios (Clase 9, 13)
    │   ├── Opciones europeas (Clase 8)
    │   └── Opciones barrera (Clase 14)
    │
    → Optimización convexa (CVXPY / DCP)
    │   ├── QP: frontera eficiente (Clase 4, 11)
    │   ├── QCQP: restricción de riesgo (Clase 15)
    │   ├── SOCP: tracking error, CML, robusta (Clase 10, 12, 15)
    │   └── Charnes-Cooper: max Sharpe (Clase 4, 9, 10)
    │
    → Programación entera (Pyomo)
        └── MILP: problema de dieta (Clase 15)
```

---

## Optimización convexa en el curso (Boyd & Vandenberghe, 2004)

| Concepto | Secciones Boyd | Clases |
|----------|:-------------:|:------:|
| Conjuntos convexos, simplex | §2.1–2.2 | 1, 4 |
| Matrices PSD, formas cuadráticas | §2.4, §3.1.5, §A.4 | 2, 4, 11 |
| Composición y max (payoff convexo) | §3.2.3–3.2.4 | 3, 14 |
| QP (frontera eficiente) | §4.4, Ej. 4.8 | 4, 9, 11 |
| SOCP (tracking error, CML, robusta) | §4.3.1–4.3.2 | 7, 10, 12, 13, 15 |
| QCQP (restricción de riesgo) | §4.4.2 | 15 |
| Optimización paramétrica | §4.7.3 | 4, 11 |
| Dualidad, Lagrangiano, precios sombra | §5.1–5.6 | 10, 11, 13 |
| Condiciones KKT | §5.5 | 11 |
| Regularización L₁, L₂, Huber | §6.1.2, §6.3 | 5, 6, 12 |
| Estimación ML/MAP de covarianza | §7.1 | 5 |
| Optimización robusta (incertidumbre) | §7.1 | 15 |
| Multi-objetivo, Pareto | §4.7.4, §6.5 | 8, 15 |
| Charnes-Cooper (prog. fraccional) | §4.3.2 + Charnes (1962) | 4, 9, 10, 13 |
| Convexo vs. entero (NP-hard) | §4.1.3 | 15 |
| Métodos de punto interior | §11.1 | 9, 11 |

---

## Estructura del repositorio

```
SimRC/
├── README.md                     ← Esta página
├── requirements.txt              ← Dependencias (Binder las instala automáticamente)
├── LICENSE.md
│
├── 01. Parte 1/                  ← Clases 1–8
│   ├── 01. Clase 1/
│   │   ├── 01Class NB.ipynb      ← Notebook ejecutable
│   │   └── README.md             ← Lectura teórica
│   ├── 02. Clase 2/
│   │   ├── 02Class NB.ipynb
│   │   └── README.md
│   └── ...
│
└── 02. Parte 2/                  ← Clases 9–15
    ├── 09. Clase 9/
    ├── ...
    └── 15. Clase 15/
        ├── 13Class NB.ipynb
        ├── README.md
        ├── portfolio_func.py     ← Funciones reutilizables (Huber + LW + CVXPY)
        ├── portfolio_bond.py     ← Portafolios con bono
        ├── diet.py               ← Modelo Pyomo (dieta, MILP)
        └── dietdata.dat
```

---

## Ejecución local

```bash
git clone https://github.com/jdsanch1/SimRC.git
cd SimRC
pip install -r requirements.txt
jupyter notebook
```

---

## Referencias principales

### Textos

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — [PDF gratuito](https://web.stanford.edu/~boyd/cvxbook/).
- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
- **McNeil, A. J., Frey, R. & Embrechts, P.** (2015). *Quantitative Risk Management* (2nd ed.). Princeton University Press.
- **Tsay, R. S.** (2010). *Analysis of Financial Time Series* (3rd ed.). Wiley.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.
- **Glasserman, P.** (2003). *Monte Carlo Methods in Financial Engineering*. Springer.
- **Birge, J. R. & Louveaux, F.** (2011). *Introduction to Stochastic Programming* (2nd ed.). Springer.

### Artículos seminales

- **Markowitz, H.** (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.
- **Sharpe, W. F.** (1964). Capital Asset Prices. *The Journal of Finance*, 19(3), 425–442.
- **Black, F. & Scholes, M.** (1973). The Pricing of Options and Corporate Liabilities. *Journal of Political Economy*, 81(3), 637–654.
- **Charnes, A. & Cooper, W. W.** (1962). Programming with linear fractional functionals. *Naval Research Logistics Quarterly*, 9(3–4), 181–186.
- **Ledoit, O. & Wolf, M.** (2004). A well-conditioned estimator for large-dimensional covariance matrices. *Journal of Multivariate Analysis*, 88(2), 365–411.
- **Huber, P. J.** (1964). Robust Estimation of a Location Parameter. *The Annals of Mathematical Statistics*, 35(1), 73–101.
- **Artzner, P., Delbaen, F., Eber, J.-M. & Heath, D.** (1999). Coherent Measures of Risk. *Mathematical Finance*, 9(3), 203–228.
- **Tobin, J.** (1958). Liquidity Preference as Behavior Towards Risk. *The Review of Economic Studies*, 25(2), 65–86.

---

## Licencia

Ver [LICENSE.md](LICENSE.md)
