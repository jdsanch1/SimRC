# Clase 10 — Inclusión de activo libre de riesgo (bono)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/10.%20Clase%2010/10Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F10.%20Clase%2010%2F10Class%20NB.ipynb)

---

## Objetivo

Extender la optimización de portafolios incorporando un **activo libre de riesgo** (bono) y derivar la **Capital Market Line** (CML).

---

## Contenido teórico

### Capital Market Line (CML)

Al incluir un bono con rendimiento r_f y varianza cero, la frontera eficiente se transforma en una **línea recta** que conecta el punto (0, r_f) con el portafolio tangente:

$$
\mu_p = r_f + \frac{\mu_T - r_f}{\sigma_T} \cdot \sigma_p
$$

donde T es el portafolio tangente (máximo Sharpe). La pendiente es el ratio de Sharpe del portafolio tangente.

### Extensión de la covarianza

La matriz de covarianza se extiende con una fila/columna de ceros para el bono (varianza = 0, covarianza = 0 con todos los activos).

---

## Referencias bibliográficas

### Optimización convexa (Boyd & Vandenberghe, 2004)

- **§4.3 Programación lineal** (pp. 146–150): Con un activo libre de riesgo, parte del problema se linealiza. La CML es la solución de un problema de optimización donde el rendimiento es lineal en la asignación al bono.

- **§5.1–5.2 Lagrangiano y dualidad** (pp. 215–233): El **multiplicador de Lagrange** asociado a la restricción Σwᵢ = 1 tiene interpretación económica: es el **precio sombra** del capital. La dualidad de Boyd formaliza cómo relajar restricciones afecta al valor óptimo.
  - Lagrangiano: L(w, λ, ν) = w'Σw - λ'w - ν(1'w - 1)
  - La variable dual ν* corresponde al costo de oportunidad del capital

- **§5.6 Precios sombra** (pp. 267–270): Boyd muestra que el multiplicador óptimo λ* indica cuánto cambia la función objetivo por unidad de relajación de la restricción. En finanzas, esto es el valor marginal de agregar capital o activos.

### Otros textos

- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press. — Cap. 6: Mean-Variance Portfolio Theory.
- **Sharpe, W. F.** (1964). Capital Asset Prices. *The Journal of Finance*, 19(3), 425–442.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

---

## Navegación del curso

← **Anterior**: Clase 9: Optimización Monte Carlo refinada
→ **Siguiente**: Clase 11: Frontera eficiente con CVXPY

---

*Archivo de apoyo para la Clase 10 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
