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

donde P = μ·Σ (Hessiana), q = -μ̄ (gradiente lineal), y las restricciones codifican Σwᵢ = 1 y w ≥ 0. El QP tiene solución global única cuando P es definida positiva (Boyd & Vandenberghe, 2004, §4.4). La frontera eficiente se construye como una familia paramétrica de QPs (Boyd & Vandenberghe, 2004, §4.7.3), aprovechando `cp.Parameter()` con `warm_start=True`.

#### Condiciones KKT para el problema de Markowitz (Boyd & Vandenberghe, 2004, §5.5.3)

**Teorema (KKT).** Sea $\mathbf{w}^*$ solucion optima del QP convexo de Markowitz con rendimiento objetivo $\mu^*$. Entonces existen multiplicadores $\lambda^* \geq 0$, $\nu^* \in \mathbb{R}$, $\boldsymbol{\eta}^* \geq 0$ que satisfacen las **cuatro condiciones KKT**:

1. **Estacionariedad:**
$$
2\Sigma \mathbf{w}^* - \lambda^* \boldsymbol{\mu} + \nu^* \mathbf{1} - \boldsymbol{\eta}^* = \mathbf{0}
$$

2. **Factibilidad primal:**
$$
\boldsymbol{\mu}^\top \mathbf{w}^* \geq \mu^*, \quad \mathbf{1}^\top \mathbf{w}^* = 1, \quad \mathbf{w}^* \geq 0
$$

3. **Factibilidad dual:**
$$
\lambda^* \geq 0, \quad \boldsymbol{\eta}^* \geq 0
$$

4. **Holgura complementaria:**
$$
\lambda^*(\boldsymbol{\mu}^\top \mathbf{w}^* - \mu^*) = 0, \quad \eta_i^* \cdot w_i^* = 0 \;\; \forall i
$$

*Bosquejo de prueba.* Para problemas convexos que satisfacen la condicion de Slater (§5.2.3), las condiciones KKT son necesarias y suficientes para optimalidad (Boyd & Vandenberghe, 2004, Thm. 5.5.3). La estacionariedad se obtiene igualando a cero el gradiente del Lagrangiano; las demas condiciones provienen de la factibilidad y la complementariedad del par primal-dual. $\square$

#### Interpretacion financiera de la holgura complementaria

La condicion $\eta_i^* \cdot w_i^* = 0$ tiene una interpretacion directa en gestion de portafolios: para cada activo $i$, **exactamente una** de dos cosas ocurre:

- **$w_i^* > 0$** (el activo esta en el portafolio): entonces $\eta_i^* = 0$, y la condicion de estacionariedad da $2(\Sigma \mathbf{w}^*)_i = \lambda^* \mu_i - \nu^*$. Esto dice que la contribucion marginal al riesgo ($2(\Sigma \mathbf{w}^*)_i$) esta en equilibrio con la recompensa marginal ajustada ($\lambda^* \mu_i - \nu^*$).

- **$w_i^* = 0$** (el activo queda fuera): entonces $\eta_i^* > 0$, lo que implica $2(\Sigma \mathbf{w}^*)_i > \lambda^* \mu_i - \nu^*$. El activo tiene un costo marginal de riesgo que **excede** su beneficio marginal de rendimiento — incluirlo empeoraria el portafolio.

Este resultado explica por que la optimizacion de Markowitz produce portafolios **concentrados**: muchos activos simplemente no ofrecen suficiente rendimiento marginal para justificar su riesgo marginal.

#### Reglas de curvatura DCP (Boyd & Vandenberghe, 2004, §3.2)

La verificacion automatica de convexidad en CVXPY se basa en **Disciplined Convex Programming** (DCP), que aplica reglas de composicion de curvatura:

| Regla | Ejemplo en CVXPY |
|-------|-----------------|
| convexa + convexa = convexa | `cp.quad_form(w, Σ) + gamma * cp.norm(w, 1)` |
| $\alpha \cdot \text{convexa} = \text{convexa}$ si $\alpha \geq 0$ | `0.5 * cp.quad_form(w, Σ)` |
| $h(\text{convexa}) = \text{convexa}$ si $h$ es convexa y no-decreciente | `cp.maximum(cp.quad_form(w, Σ), 0)` |
| afin es convexa **y** concava | `mu_vec @ w` puede ir en objetivo o restriccion |
| concava en restriccion $\geq$ es convexa | `mu_vec @ w >= mu_target` es DCP-valido |

En la verificacion DCP del problema de Markowitz: `cp.quad_form(w, Σ)` es convexa porque $\Sigma \succeq 0$, y `mu_vec @ w` es afín; su suma ponderada preserva convexidad por la primera regla. Los multiplicadores duales del problema tienen interpretación financiera como precios de equilibrio (Boyd & Vandenberghe, 2004, §5.9).

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
