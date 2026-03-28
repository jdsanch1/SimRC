# Simulación de Riesgos y Coberturas

**[Juan Diego Sánchez Torres](https://www.researchgate.net/profile/Juan_Diego_Sanchez_Torres)**
Profesor — [MAF ITESO](http://maf.iteso.mx/web/general/detalle?group_id=5858156)
dsanchez@iteso.mx

---

## Presentación del curso

Este curso cubre los fundamentos cuantitativos de la **gestión de riesgos financieros** y la **construcción de portafolios**, desde la descarga de datos de mercado hasta la optimización convexa y la valuación de derivados por simulación.

### Enfoque pedagógico

El curso combina tres pilares:

1. **Teoría financiera**: rendimientos, volatilidad, opciones, frontera eficiente de Markowitz, VaR/CVaR.
2. **Optimización convexa**: programación cuadrática (QP), programación convexa disciplinada (DCP), dualidad y condiciones KKT, basado en Boyd & Vandenberghe (2004).
3. **Implementación en Python**: cada concepto se acompaña de código ejecutable con datos reales de mercado.

### Herramientas

- **[CVXPY](https://www.cvxpy.org/)** — Optimización convexa con verificación automática de convexidad (DCP).
- **[Pyomo](https://www.pyomo.org/)** — Programación matemática general (MILP, programación estocástica).
- **[yfinance](https://github.com/ranaroussi/yfinance)** — Descarga de datos de Yahoo Finance.
- **[scikit-learn](https://scikit-learn.org/)** — Estimadores robustos (Ledoit-Wolf, KDE, K-Means).
- **[statsmodels](https://www.statsmodels.org/)** — Estimador de Huber para media robusta.

### Ejecución en la nube

Todos los notebooks se pueden ejecutar directamente en **Google Colab** o **Binder** (JupyterLab en la nube, sin necesidad de cuenta Google) usando los botones de la tabla de abajo.

---

## Contenido del curso

### Parte 1 — Portafolios, estimación robusta y simulación Monte Carlo

| Clase | Tema | Notebook | Lectura |
|:-----:|------|:--------:|:-------:|
| 1 | Análisis de acciones con Python | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/01.%20Clase%201/01Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F01.%20Clase%201%2F01Class%20NB.ipynb) | [README](01.%20Parte%201/01.%20Clase%201/) |
| 2 | Retornos logarítmicos y matriz de covarianza | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/02.%20Clase%202/02Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F02.%20Clase%202%2F02Class%20NB.ipynb) | [README](01.%20Parte%201/02.%20Clase%202/) |
| 3 | Opciones financieras: payoff, P&L y volatilidad implícita | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/03.%20Clase%203/03Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F03.%20Clase%203%2F03Class%20NB.ipynb) | [README](01.%20Parte%201/03.%20Clase%203/) |
| 4 | Ratio de Sharpe y portafolio óptimo (CVXPY/DCP) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/04.%20Clase%204/04Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F04.%20Clase%204%2F04Class%20NB.ipynb) | [README](01.%20Parte%201/04.%20Clase%204/) |
| 5 | Covarianza robusta (Shrunk Covariance / Ledoit-Wolf) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/05.%20Clase%205/05Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F05.%20Clase%205%2F05Class%20NB.ipynb) | [README](01.%20Parte%201/05.%20Clase%205/) |
| 6 | Media robusta (estimador de Huber) y generación de números aleatorios | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/06.%20Clase%206/06Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F06.%20Clase%206%2F06Class%20NB.ipynb) | [README](01.%20Parte%201/06.%20Clase%206/) |
| 7 | Comparación de estimadores y análisis de riesgo (VaR/CVaR) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/07.%20Clase%207/07Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F07.%20Clase%207%2F07Class%20NB.ipynb) | [README](01.%20Parte%201/07.%20Clase%207/) |
| 8 | Resumen Parte 1 — Valuación de opciones por simulación MC | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/08.%20Clase%208/08Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F08.%20Clase%208%2F08Class%20NB.ipynb) | [README](01.%20Parte%201/08.%20Clase%208/) |

### Parte 2 — Optimización avanzada y productos derivados

| Clase | Tema | Notebook | Lectura |
|:-----:|------|:--------:|:-------:|
| 9 | Optimización Monte Carlo refinada | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/09.%20Clase%209/09Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F09.%20Clase%209%2F09Class%20NB.ipynb) | [README](02.%20Parte%202/09.%20Clase%209/) |
| 10 | Inclusión de activo libre de riesgo (bono) y Capital Market Line | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/10.%20Clase%2010/10Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F10.%20Clase%2010%2F10Class%20NB.ipynb) | [README](02.%20Parte%202/10.%20Clase%2010/) |
| 11 | Frontera eficiente Markowitz con CVXPY (DCP) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/11.%20Clase%2011/11Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F11.%20Clase%2011%2F11Class%20NB.ipynb) | [README](02.%20Parte%202/11.%20Clase%2011/) |
| 12 | Optimización avanzada de portafolios | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/12.%20Clase%2012/12Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F12.%20Clase%2012%2F12Class%20NB.ipynb) | [README](02.%20Parte%202/12.%20Clase%2012/) |
| 13 | Portafolio con bono — Monte Carlo vs Markowitz | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/13.%20Clase%2013/13Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F13.%20Clase%2013%2F13Class%20NB.ipynb) | [README](02.%20Parte%202/13.%20Clase%2013/) |
| 14 | Opciones barrera (knock-in / knock-out) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/14.%20Clase%2014/14Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F14.%20Clase%2014%2F14Class%20NB.ipynb) | [README](02.%20Parte%202/14.%20Clase%2014/) |
| 15 | Programación estocástica con Pyomo y CVXPY | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/15.%20Clase%2015/13Class%20NB.ipynb) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F15.%20Clase%2015%2F13Class%20NB.ipynb) | [README](02.%20Parte%202/15.%20Clase%2015/) |

---

## Estructura del repositorio

```
SimRC/
├── requirements.txt              ← Dependencias (Binder las instala automáticamente)
├── 01. Parte 1/
│   ├── 01. Clase 1/
│   │   ├── 01Class NB.ipynb      ← Notebook ejecutable (Colab / Binder / local)
│   │   └── README.md             ← Lectura teórica con definiciones, teoremas y referencias
│   ├── 02. Clase 2/
│   │   ├── 02Class NB.ipynb
│   │   └── README.md
│   ├── ...
│   └── 08. Clase 8/
└── 02. Parte 2/
    ├── 09. Clase 9/
    ├── ...
    ├── 15. Clase 15/
    │   ├── 13Class NB.ipynb
    │   ├── README.md
    │   ├── portfolio_func.py     ← Funciones reutilizables de portafolios
    │   ├── portfolio_bond.py     ← Portafolios con bono
    │   ├── diet.py               ← Modelo Pyomo (problema de dieta)
    │   └── dietdata.dat
    └── ...
```

Cada carpeta de clase contiene:
- **Notebook** (`.ipynb`): código ejecutable con datos reales, gráficos y explicaciones.
- **README** (`.md`): lectura teórica complementaria con definiciones formales, teoremas, pruebas matemáticas y referencias bibliográficas.

---

## Temas cubiertos

### Finanzas cuantitativas

- Descarga de precios históricos con `yfinance`
- Rendimientos logarítmicos, volatilidad móvil, correlación rodante
- Opciones financieras: payoff, P&L, volatilidad implícita, paridad put-call, Black-Scholes
- Frontera eficiente de Markowitz y ratio de Sharpe
- Estimadores robustos: Shrunk Covariance (Ledoit-Wolf), estimador de Huber
- Simulación Monte Carlo: portafolios, valuación de opciones, opciones barrera
- Medidas de riesgo: VaR y CVaR (Expected Shortfall)
- Capital Market Line y activo libre de riesgo
- Programación estocástica (Pyomo)

### Optimización convexa (Boyd & Vandenberghe, 2004)

- Conjuntos convexos, funciones convexas, formas cuadráticas (Cap. 2–3)
- Programación cuadrática (QP) y cónica (SOCP) (Cap. 4)
- Programación convexa disciplinada (DCP) con CVXPY
- Dualidad, condiciones KKT, precios sombra (Cap. 5)
- Regularización (L₁, L₂, Huber) y estimación robusta (Cap. 6–7)
- Optimización multi-objetivo y frontera de Pareto

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

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — [Libro completo (PDF gratuito)](https://web.stanford.edu/~boyd/cvxbook/).
- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
- **Markowitz, H.** (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.
- **Tsay, R. S.** (2010). *Analysis of Financial Time Series* (3rd ed.). Wiley.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

---

## Licencia

Ver [LICENSE.md](LICENSE.md)
