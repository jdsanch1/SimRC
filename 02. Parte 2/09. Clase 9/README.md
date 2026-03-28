# Clase 9 — Optimización Monte Carlo refinada

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/09.%20Clase%209/09Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F09.%20Clase%209%2F09Class%20NB.ipynb)

---

## Objetivo

Refinar la simulación Monte Carlo de portafolios incorporando estimadores robustos (Huber + Ledoit-Wolf) y comparar con la optimización determinista de Markowitz.

---

## Contenido teórico

### Simulación Monte Carlo de portafolios

Se generan N portafolios con pesos aleatorios (distribución de Dirichlet) y se evalúa el rendimiento y riesgo de cada uno usando estimadores robustos. En la práctica, los portafolios pueden tener restricciones adicionales (límites sectoriales, posiciones máximas, turnover) que, al ser lineales, preservan la convexidad del QP (Boyd & Vandenberghe, 2004, §4.4). Restricciones cuadráticas como el tracking error convierten el problema en un QCQP que sigue siendo convexo (Boyd & Vandenberghe, 2004, §4.6).

### Comparación MC vs. optimización

| Método | Ventaja | Limitación |
|--------|---------|------------|
| Monte Carlo | Explora todo el espacio factible | Ineficiente para encontrar el óptimo |
| Markowitz (QP) | Encuentra el óptimo exacto (Boyd & Vandenberghe, 2004, §4.4) | Sensible a errores de estimación |
| MC + estimadores robustos | Explora con parámetros estables | No garantiza optimalidad |

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §4.4 (QP con restricciones), §4.6 (QCQP), §11.1 (métodos de punto interior usados por los solvers de CVXPY).
- **Glasserman, P.** (2003). *Monte Carlo Methods in Financial Engineering*. Springer.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

---

## Navegación del curso

← **Anterior**: Clase 8: Resumen Parte 1
→ **Siguiente**: Clase 10: Inclusión de activo libre de riesgo

---

*Archivo de apoyo para la Clase 9 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
