# Clase 13 — Portafolio con bono: comparación Monte Carlo vs Markowitz

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/13.%20Clase%2013/13Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F13.%20Clase%2013%2F13Class%20NB.ipynb)

---

## Objetivo

Comparar la simulación Monte Carlo con la optimización de Markowitz para portafolios que incluyen un activo libre de riesgo (bono), usando tres métodos de simulación de rendimientos (normal, histograma, KDE). La CML se puede derivar como la solución de un SOCP (Boyd & Vandenberghe, 2004, §4.3.2), y los multiplicadores duales del problema de optimización tienen interpretación como precios sombra (Boyd & Vandenberghe, 2004, §5.6): el precio sombra de la restricción de riesgo es exactamente el ratio de Sharpe del portafolio tangente.

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §4.3.2 (SOCP y CML), §5.6 (precios sombra).
- **Glasserman, P.** (2003). *Monte Carlo Methods in Financial Engineering*. Springer.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
- **Markowitz, H.** (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

---

## Navegación del curso

← **Anterior**: Clase 12: Optimización avanzada
→ **Siguiente**: Clase 14: Opciones barrera

---

*Archivo de apoyo para la Clase 13 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
