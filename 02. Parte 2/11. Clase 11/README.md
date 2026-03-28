# Clase 11 — Frontera eficiente Markowitz con CVXPY

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/11.%20Clase%2011/11Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F11.%20Clase%2011%2F11Class%20NB.ipynb)

---

## Objetivo

Implementar la frontera eficiente completa usando funciones reutilizables (`portfolio_func.py`) con estimadores robustos (Huber + Ledoit-Wolf) y optimización convexa (CVXPY/DCP).

---

## Contenido teórico

### Esta es una de las clases centrales de Boyd en el curso.

### Programación cuadrática (QP) en detalle

El problema de Markowitz en forma estándar QP (Boyd §4.4):

$$
\min_{\mathbf{w}} \quad \frac{1}{2} \mathbf{w}^\top P \mathbf{w} + q^\top \mathbf{w}
$$

sujeto a: Gw ≤ h, Aw = b

donde P = μ·Σ (Hessiana), q = -μ̄ (gradiente lineal), y las restricciones codifican Σwᵢ = 1 y w ≥ 0.

---

## Referencias bibliográficas

### Optimización convexa (Boyd & Vandenberghe, 2004)

- **§4.4 Programación cuadrática** (pp. 152–154): Boyd formaliza el QP convexo y demuestra que tiene solución global única cuando P ≻ 0 (definida positiva). El problema de Markowitz satisface esta condición cuando Σ tiene rango completo.

- **§4.7.3 Optimización paramétrica** (pp. 181–182): La frontera eficiente es un ejemplo de **familia paramétrica de problemas**: para cada valor de μ*, se resuelve un QP. Boyd demuestra que la función de valor óptimo p*(μ*) es convexa, lo que garantiza que la frontera es suave y continua.
  - En CVXPY: `cp.Parameter()` con `warm_start=True` explota esta estructura

- **§5.5 Condiciones KKT** (pp. 243–252): Las condiciones de Karush-Kuhn-Tucker caracterizan la optimalidad de los portafolios:
  - Estacionariedad: 2Σw* - λ*μ - ν*1 = 0
  - Factibilidad primal: Σw*ᵢ = 1, w* ≥ 0
  - Complementariedad: w*ᵢ · sᵢ = 0 (si un activo tiene peso 0, su condición marginal no es activa)
  - Las condiciones KKT explican **por qué** ciertos activos no entran en el portafolio óptimo

- **§5.9 Dualidad y portafolios** (p. 280): El problema dual del QP de Markowitz tiene interpretación financiera: los multiplicadores duales representan los precios de equilibrio de los activos en el mercado.

### Otros textos

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — **Capítulos 4 y 5 completos**.
- **Ledoit, O. & Wolf, M.** (2004). *Journal of Multivariate Analysis*, 88(2), 365–411.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
- **Markowitz, H.** (1952). Portfolio Selection. *The Journal of Finance*, 7(1), 77–91.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

---

## Navegación del curso

← **Anterior**: Clase 10: Activo libre de riesgo
→ **Siguiente**: Clase 12: Optimización avanzada de portafolios

---

*Archivo de apoyo para la Clase 11 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
