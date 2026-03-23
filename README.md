# Simulación de Riesgos y Coberturas

**[Juan Diego Sánchez Torres](https://www.researchgate.net/profile/Juan_Diego_Sanchez_Torres)**
Profesor — [MAF ITESO](http://maf.iteso.mx/web/general/detalle?group_id=5858156)
dsanchez@iteso.mx

Notebooks del curso de simulación y riesgo aplicado a finanzas. Cubren desde los fundamentos de teoría de portafolios hasta opciones exóticas y optimización estocástica.

---

## Abrir en Google Colab

Haz clic en el botón de la clase que quieras explorar:

### Parte 1 — Portafolios y Simulación Monte Carlo

| Clase | Tema | Colab |
|-------|------|-------|
| 1 | Introducción, descarga de datos, simulación Monte Carlo básica | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/01.%20Clase%201/01Class%20NB.ipynb) |
| 2 | Retornos logarítmicos y matriz de covarianza | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/02.%20Clase%202/02Class%20NB.ipynb) |
| 3 | Frontera eficiente con Monte Carlo | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/03.%20Clase%203/03Class%20NB.ipynb) |
| 4 | Ratio de Sharpe y portafolio óptimo | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/04.%20Clase%204/04Class%20NB.ipynb) |
| 5 | Covarianza robusta (Shrunk Covariance) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/05.%20Clase%205/05Class%20NB.ipynb) |
| 6 | Media robusta (estimador de Huber) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/06.%20Clase%206/06Class%20NB.ipynb) |
| 7 | Comparación de estimadores y análisis de riesgo | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/07.%20Clase%207/07Class%20NB.ipynb) |
| 8 | Resumen Parte 1 y consolidación de funciones | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/08.%20Clase%208/08Class%20NB.ipynb) |

### Parte 2 — Optimización y Productos Derivados

| Clase | Tema | Colab |
|-------|------|-------|
| 9  | Optimización Monte Carlo refinada | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/09.%20Clase%209/09Class%20NB.ipynb) |
| 10 | Inclusión de activo libre de riesgo (bono) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/10.%20Clase%2010/10Class%20NB.ipynb) |
| 11 | Frontera eficiente Markowitz con `cvxopt` | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/11.%20Clase%2011/11Class%20NB.ipynb) |
| 12 | Optimización avanzada de portafolios | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/12.%20Clase%2012/12Class%20NB.ipynb) |
| 13 | Portafolio con bono — comparación Monte Carlo vs Markowitz | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/13.%20Clase%2013/13Class%20NB.ipynb) |
| 14 | Opciones barrera (knock-in / knock-out) | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/14.%20Clase%2014/14Class%20NB.ipynb) |
| 15 | Programación estocástica con Pyomo | [![Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/15.%20Clase%2015/13Class%20NB.ipynb) |

---

## Estructura del repositorio

```
SimRC/
├── 01. Parte 1/
│   ├── 01. Clase 1/
│   ├── 02. Clase 2/
│   ├── 03. Clase 3/
│   ├── 04. Clase 4/
│   ├── 05. Clase 5/
│   ├── 06. Clase 6/
│   ├── 07. Clase 7/
│   └── 08. Clase 8/
└── 02. Parte 2/
    ├── 09. Clase 9/
    ├── 10. Clase 10/
    ├── 11. Clase 11/
    ├── 12. Clase 12/
    ├── 13. Clase 13/
    ├── 14. Clase 14/
    └── 15. Clase 15/
```

## Ejecución local

```bash
git clone https://github.com/jdsanch1/SimRC.git
cd SimRC
pip install yfinance pandas numpy matplotlib seaborn scipy scikit-learn statsmodels cvxopt pyomo
jupyter notebook
```

## Temas cubiertos

- Descarga de precios históricos con `yfinance`
- Retornos logarítmicos y matriz de covarianza
- Estimadores robustos (Huber, Shrunk Covariance)
- Simulación Monte Carlo de portafolios
- Ratio de Sharpe y frontera eficiente
- Optimización cuadrática (Markowitz) con `cvxopt`
- Inclusión de activo libre de riesgo
- Opciones barrera (path-dependent options)
- Programación estocástica con `pyomo`

## Licencia

Ver [LICENSE.md](LICENSE.md)
