# Clase 9 — Optimización Monte Carlo refinada

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/09.%20Clase%209/09Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F09.%20Clase%209%2F09Class%20NB.ipynb)

---

## Objetivo

Refinar la simulación Monte Carlo de portafolios incorporando estimadores robustos (Huber + Ledoit-Wolf) y comparar con la optimización determinista de Markowitz.

---

## Contenido teórico

### Simulación Monte Carlo de portafolios

Se generan N portafolios con pesos aleatorios (distribución de Dirichlet) y se evalúa el rendimiento y riesgo de cada uno usando estimadores robustos.

### Comparación MC vs. optimización

| Método | Ventaja | Limitación |
|--------|---------|------------|
| Monte Carlo | Explora todo el espacio factible | Ineficiente para encontrar el óptimo |
| Markowitz (QP) | Encuentra el óptimo exacto | Sensible a errores de estimación |
| MC + estimadores robustos | Explora con parámetros estables | No garantiza optimalidad |

---

## Referencias bibliográficas

### Optimización convexa (Boyd & Vandenberghe, 2004)

- **§4.4 Programación cuadrática con restricciones adicionales** (pp. 152–154): En la práctica, los portafolios tienen restricciones adicionales a Σwᵢ = 1 y w ≥ 0: límites sectoriales, posiciones máximas, turnover. Boyd muestra que agregar restricciones lineales a un QP preserva la convexidad.

- **§4.6 QCQP** (pp. 166–167): Cuando las restricciones son cuadráticas (e.g., tracking error ≤ ε), el problema se convierte en QCQP (Quadratically Constrained QP), que sigue siendo convexo si las restricciones son convexas.

- **§11.1 Métodos de barrera** (pp. 561–568): Los solvers internos de CVXPY (ECOS, SCS) usan métodos de punto interior. Boyd explica cómo estos métodos resuelven QPs transformando restricciones de desigualdad en penalizaciones logarítmicas.

### Otros textos

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
