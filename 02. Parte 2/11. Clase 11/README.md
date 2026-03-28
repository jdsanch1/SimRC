# Clase 11 — Frontera eficiente Markowitz con CVXPY

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/11.%20Clase%2011/11Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F11.%20Clase%2011%2F11Class%20NB.ipynb)

---

## Objetivo

Implementar la frontera eficiente completa usando funciones reutilizables (`portfolio_func.py`) con estimadores robustos (Huber + Ledoit-Wolf) y optimización convexa (CVXPY/DCP).

---

## Contenido teórico

### Programación cuadrática (QP) en detalle

El problema de Markowitz en forma estándar QP (Boyd & Vandenberghe, 2004, §4.4):

$$
\min_{\mathbf{w}} \quad \frac{1}{2} \mathbf{w}^\top P \mathbf{w} + q^\top \mathbf{w}
$$

sujeto a: Gw ≤ h, Aw = b

donde P = μ·Σ (Hessiana), q = -μ̄ (gradiente lineal), y las restricciones codifican Σwᵢ = 1 y w ≥ 0. El QP tiene solución global única cuando P es definida positiva (Boyd & Vandenberghe, 2004, §4.4). La frontera eficiente se construye como una familia paramétrica de QPs (Boyd & Vandenberghe, 2004, §4.7.3), aprovechando `cp.Parameter()` con `warm_start=True`. Las condiciones KKT (Boyd & Vandenberghe, 2004, §5.5) caracterizan la optimalidad y explican por qué ciertos activos quedan fuera del portafolio óptimo: la complementariedad $w_i^* \cdot s_i = 0$ implica que un activo con peso cero tiene su condición marginal inactiva. Los multiplicadores duales del problema tienen interpretación financiera como precios de equilibrio (Boyd & Vandenberghe, 2004, §5.9). En la verificación DCP (Boyd & Vandenberghe, 2004, §3.2), `cp.quad_form(w, Σ)` es convexa porque $\Sigma \succeq 0$, y `mu_vec @ w` es afín.

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — Cap. 3–5 (reglas DCP, QP, optimización paramétrica, dualidad, KKT), Cap. 11 (métodos de punto interior).
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
