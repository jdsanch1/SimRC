# Clase 13 — Portafolio con bono: comparación Monte Carlo vs Markowitz

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/13.%20Clase%2013/13Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F13.%20Clase%2013%2F13Class%20NB.ipynb)

---

## Objetivo

Comparar la simulación Monte Carlo con la optimización de Markowitz para portafolios que incluyen un activo libre de riesgo (bono), usando tres métodos de simulación de rendimientos (normal, histograma, KDE).

---

## Referencias bibliográficas

### Optimización convexa (Boyd & Vandenberghe, 2004)

- **§4.3.2 SOCP y Capital Market Line** (pp. 156–158): La CML se puede derivar como la solución de un SOCP donde se maximiza el rendimiento sujeto a una restricción cónica sobre el riesgo.

- **§5.6 Precios sombra** (pp. 267–270): En la comparación MC vs. Markowitz, los multiplicadores duales del problema de optimización tienen interpretación directa: el precio sombra de la restricción de riesgo indica cuánto rendimiento adicional se obtiene por unidad de riesgo adicional permitido — que es exactamente el ratio de Sharpe del portafolio tangente.

### Otros textos

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
