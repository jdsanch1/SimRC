# Clase 13 — Portafolio con bono: comparación Monte Carlo vs Markowitz

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/13.%20Clase%2013/13Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F13.%20Clase%2013%2F13Class%20NB.ipynb)

---

## Objetivo

Comparar la simulación Monte Carlo con la optimización de Markowitz para portafolios que incluyen un activo libre de riesgo (bono), usando tres métodos de simulación de rendimientos (normal, histograma, KDE).

---

## Contenido teórico

### CML como SOCP via transformación de Charnes-Cooper (Boyd & Vandenberghe, 2004, §4.3.2)

El portafolio tangente (maximo Sharpe ratio) se formula originalmente como un problema fraccional no convexo:

$$
\max_{\mathbf{w}} \; \frac{\boldsymbol{\mu}^\top \mathbf{w} - r_f}{\sqrt{\mathbf{w}^\top \Sigma \mathbf{w}}} \quad \text{s.a.} \quad \mathbf{1}^\top \mathbf{w} = 1, \; \mathbf{w} \geq 0
$$

**Teorema (Charnes-Cooper, 1962).** La transformacion $\mathbf{y} = t \mathbf{w}$, $t = 1/(\mathbf{1}^\top \mathbf{w})$ convierte el problema fraccional en un **SOCP** equivalente:

$$
\max_{\mathbf{y}, t} \; \boldsymbol{\mu}^\top \mathbf{y} - r_f \cdot t \quad \text{s.a.} \quad \| \Sigma^{1/2} \mathbf{y} \|_2 \leq 1, \; \mathbf{1}^\top \mathbf{y} = t, \; t \geq 0, \; \mathbf{y} \geq 0
$$

*Bosquejo de prueba.* Sea $\mathbf{w}$ factible con $\mathbf{1}^\top \mathbf{w} > 0$. Definiendo $t = (\mathbf{1}^\top \mathbf{w})^{-1}$ y $\mathbf{y} = t\mathbf{w}$, se tiene $\mathbf{1}^\top \mathbf{y} = t$ y el denominador del Sharpe ratio se normaliza a $\|\Sigma^{1/2}\mathbf{y}\|_2 / t$. Fijando $\|\Sigma^{1/2}\mathbf{y}\|_2 = 1$, maximizar el numerador $\boldsymbol{\mu}^\top \mathbf{y} - r_f t$ es equivalente a maximizar el ratio original. La restriccion $\|\Sigma^{1/2}\mathbf{y}\|_2 \leq 1$ define un cono de segundo orden, y el objetivo es lineal en $(\mathbf{y}, t)$, lo que hace del problema un SOCP (Boyd & Vandenberghe, 2004, §4.3.2). $\square$

*Interpretacion financiera.* La CML completa se obtiene combinando la solucion $\mathbf{w}^* = \mathbf{y}^*/t^*$ (portafolio tangente) con el activo libre de riesgo. Todo portafolio eficiente es una mezcla $\alpha \mathbf{w}^* + (1-\alpha) \mathbf{e}_{r_f}$ con $\alpha \in [0, +\infty)$, donde $\alpha > 1$ representa apalancamiento.

### Precio sombra de la restricción de riesgo = Sharpe ratio (Boyd & Vandenberghe, 2004, §5.6)

**Teorema.** Considere el problema de maximizar rendimiento sujeto a una cota de riesgo:

$$
\max_{\mathbf{w}} \; \boldsymbol{\mu}^\top \mathbf{w} \quad \text{s.a.} \quad \sqrt{\mathbf{w}^\top \Sigma \mathbf{w}} \leq \sigma_{\max}, \; \mathbf{1}^\top \mathbf{w} = 1, \; \mathbf{w} \geq 0
$$

Si $\lambda^*$ es el multiplicador dual optimo de la restriccion de riesgo, entonces:

$$
\lambda^* = \frac{\partial \mu^*_p}{\partial \sigma_{\max}} = \frac{\mu_T - r_f}{\sigma_T} = \text{Sharpe ratio del portafolio tangente}
$$

*Bosquejo de prueba.* Por el teorema de sensibilidad de Boyd & Vandenberghe (2004, §5.6.2), el multiplicador optimo $\lambda^*$ mide la tasa de cambio del valor optimo respecto a la perturbacion del lado derecho de la restriccion. En la frontera eficiente, $\mu^*_p(\sigma_{\max})$ es localmente lineal con pendiente $(\mu_T - r_f)/\sigma_T$ en la region de la CML. Por tanto, $\lambda^* = (\mu_T - r_f)/\sigma_T$. $\square$

*Interpretacion financiera.* Este resultado conecta la teoria de dualidad con la medida de desempeno mas usada en la industria: cada unidad adicional de riesgo permitida genera exactamente un Sharpe ratio de rendimiento adicional. Si el Sharpe es 0.8, permitir 1% mas de volatilidad genera 0.8% mas de rendimiento esperado.

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
