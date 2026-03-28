# Clase 12 — Optimización avanzada de portafolios

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/12.%20Clase%2012/12Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F12.%20Clase%2012%2F12Class%20NB.ipynb)

---

## Objetivo

Explorar extensiones del modelo de Markowitz: restricciones de tracking error, regularización de pesos, y estrategias de opciones.

---

## Referencias bibliográficas

### Optimización convexa (Boyd & Vandenberghe, 2004)

- **§4.3.1 SOCP** (pp. 156–158): Las restricciones de **tracking error** (desviación respecto a un benchmark) se formulan como SOCP:
  - ||Σ^(1/2)(w - w_bench)||₂ ≤ ε
  - Esta es una restricción de cono de segundo orden, más general que las lineales del QP estándar

- **§4.6 QCQP** (pp. 166–167): Restricciones cuadráticas adicionales (e.g., límites de riesgo sectorial) mantienen la convexidad si cada restricción es convexa individualmente.

- **§6.3.2 Regularización Tikhonov** (pp. 305–306): Agregar ||w||₂² al objetivo estabiliza los pesos:
  - min w'Σw + λ||w||₂² — los pesos se "encogen" hacia cero
  - Equivalente a un prior gaussiano sobre los pesos (interpretación bayesiana)
  - En CVXPY: `cp.norm(w, 2)**2` es DCP-convexo

- **§6.3.1 Regularización L₁** (p. 305): La penalización ||w||₁ promueve **esparcidad** (portafolios con pocos activos activos):
  - min w'Σw + λ||w||₁ — genera portafolios "sparse"
  - En CVXPY: `cp.norm(w, 1)` es DCP-convexo

### Otros textos

- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

---

## Navegación del curso

← **Anterior**: Clase 11: Frontera eficiente con CVXPY
→ **Siguiente**: Clase 13: Portafolio con bono (MC vs Markowitz)

---

*Archivo de apoyo para la Clase 12 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
