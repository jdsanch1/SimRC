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

donde T es el portafolio tangente (máximo Sharpe). La pendiente es el ratio de Sharpe del portafolio tangente. Con el activo libre de riesgo, parte del problema se linealiza (Boyd & Vandenberghe, 2004, §4.3).

#### Lagrangiano del problema de Markowitz (Boyd & Vandenberghe, 2004, §5.1)

**Definicion.** Para el problema de minima varianza con rendimiento objetivo $\mu^*$:

$$
\min_{\mathbf{w}} \; \mathbf{w}^\top \Sigma \mathbf{w} \quad \text{s.a.} \quad \boldsymbol{\mu}^\top \mathbf{w} \geq \mu^*, \; \mathbf{1}^\top \mathbf{w} = 1, \; \mathbf{w} \geq 0
$$

el **Lagrangiano** es:

$$
L(\mathbf{w}, \lambda, \nu, \boldsymbol{\eta}) = \mathbf{w}^\top \Sigma \mathbf{w} - \lambda(\boldsymbol{\mu}^\top \mathbf{w} - \mu^*) + \nu(\mathbf{1}^\top \mathbf{w} - 1) - \boldsymbol{\eta}^\top \mathbf{w}
$$

donde $\lambda \geq 0$ es el multiplicador de la restriccion de rendimiento, $\nu \in \mathbb{R}$ es el multiplicador de la restriccion de presupuesto, y $\boldsymbol{\eta} \geq 0$ son los multiplicadores de no-negatividad. El **dual de Lagrange** $g(\lambda, \nu, \boldsymbol{\eta}) = \inf_{\mathbf{w}} L(\mathbf{w}, \lambda, \nu, \boldsymbol{\eta})$ proporciona cotas inferiores al valor optimo primal para todo $\lambda \geq 0$, $\boldsymbol{\eta} \geq 0$.

#### Precio sombra e interpretacion financiera (Boyd & Vandenberghe, 2004, §5.6)

**Teorema (sensibilidad).** Si $p^*(\mu^*)$ es el valor optimo (varianza minima) como funcion del rendimiento objetivo $\mu^*$, entonces bajo condiciones de regularidad:

$$
\lambda^* = -\frac{\partial p^*}{\partial \mu^*}
$$

*Bosquejo de prueba.* Sea $p^*(\mu^*) = \inf_{\mathbf{w}} \{ \mathbf{w}^\top \Sigma \mathbf{w} \mid \boldsymbol{\mu}^\top \mathbf{w} \geq \mu^*, \ldots \}$. Al perturbar $\mu^* \to \mu^* + \delta$, la teoria de dualidad muestra que $p^*(\mu^* + \delta) \approx p^*(\mu^*) - \lambda^* \delta$ para $\delta$ pequeno (Boyd & Vandenberghe, 2004, §5.6.2). $\square$

*Interpretacion financiera.* El multiplicador $\lambda^*$ mide cuantas unidades de varianza se reducen al relajar en una unidad la meta de rendimiento. Es la **tasa marginal de sustitucion** entre riesgo y rendimiento en la frontera eficiente — un $\lambda^*$ grande indica que estamos en la zona de alta pendiente de la frontera, donde pequenos sacrificios de rendimiento producen grandes reducciones de riesgo.

#### Dualidad fuerte y condicion de Slater (Boyd & Vandenberghe, 2004, §5.2.3)

**Teorema (dualidad fuerte bajo Slater).** Si el problema primal es convexo y existe un punto **estrictamente factible** $\tilde{\mathbf{w}}$ tal que $f_i(\tilde{\mathbf{w}}) < 0$ para toda restriccion de desigualdad (condicion de Slater), entonces el **gap de dualidad es cero**: $d^* = p^*$.

*Bosquejo de prueba.* La condicion de Slater garantiza que el conjunto de restricciones calificadas se satisface, lo que implica que el hiperplano separador entre los conjuntos epigrafo del primal y los semiespacios del dual existe y es tangente (Boyd & Vandenberghe, 2004, §5.2.3, Thm. 5.2). $\square$

*Aplicacion a Markowitz.* Cualquier portafolio uniformemente diversificado $\tilde{w}_i = 1/n$ con $\boldsymbol{\mu}^\top \tilde{\mathbf{w}} > \mu^*$ es un punto estrictamente factible, ya que satisface las desigualdades con holgura estricta. Esto garantiza gap de dualidad cero y que los precios sombra $\lambda^*$, $\nu^*$ tienen interpretacion economica exacta (no aproximada).

### Extensión de la covarianza

La matriz de covarianza se extiende con una fila/columna de ceros para el bono (varianza = 0, covarianza = 0 con todos los activos).

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §4.3 (programación lineal), §5.1–5.2, §5.6 (dualidad y precios sombra).
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
