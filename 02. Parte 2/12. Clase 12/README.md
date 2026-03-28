# Clase 12 — Optimización avanzada de portafolios

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/12.%20Clase%2012/12Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F12.%20Clase%2012%2F12Class%20NB.ipynb)

---

## Objetivo

Explorar extensiones del modelo de Markowitz: restricciones de tracking error, regularización de pesos, y estrategias de opciones.

---

## Contenido teórico

### Regularización L₂ — Tikhonov (Boyd & Vandenberghe, 2004, §6.3.2)

La regularización L₂ (ridge / Tikhonov) agrega un término cuadrático de penalización al objetivo de Markowitz:

$$
\min_{\mathbf{w}} \quad \mathbf{w}^\top \Sigma \mathbf{w} + \gamma \|\mathbf{w}\|_2^2
$$

sujeto a:

$$
\boldsymbol{\mu}^\top \mathbf{w} \geq \mu^*, \qquad \sum_i w_i = 1, \qquad w_i \geq 0
$$

donde $\gamma > 0$ es el hiperparámetro de regularización. Esto equivale a resolver el QP con la matriz $\Sigma + \gamma I$ en lugar de $\Sigma$.

**Convexidad.** La norma al cuadrado $\|\mathbf{w}\|_2^2 = \mathbf{w}^\top I \, \mathbf{w}$ es convexa (pues $I \succ 0$). La suma de dos funciones convexas es convexa (Boyd §3.2.1), así que $\mathbf{w}^\top(\Sigma + \gamma I)\mathbf{w}$ es convexa. ∎

**Interpretación financiera:**

1. **Mejora del condicionamiento.** Si $\Sigma$ tiene autovalores $\lambda_1 \geq \cdots \geq \lambda_n > 0$, el número de condición pasa de $\kappa(\Sigma) = \lambda_1/\lambda_n$ a $\kappa(\Sigma + \gamma I) = (\lambda_1 + \gamma)/(\lambda_n + \gamma)$, que es estrictamente menor. Esto reduce la sensibilidad de los pesos óptimos a errores de estimación.

2. **Shrinkage hacia equi-ponderación.** El término $\gamma \|\mathbf{w}\|_2^2$ penaliza posiciones extremas, empujando la solución hacia pesos más uniformes — un efecto similar al estimador Ledoit-Wolf pero implementado vía optimización.

### Regularización L₁ — Esparcidad (Boyd & Vandenberghe, 2004, §6.3.1)

La regularización L₁ (LASSO) promueve **esparcidad** en los pesos del portafolio:

$$
\min_{\mathbf{w}} \quad \mathbf{w}^\top \Sigma \mathbf{w} + \gamma \|\mathbf{w}\|_1
$$

sujeto a:

$$
\boldsymbol{\mu}^\top \mathbf{w} \geq \mu^*, \qquad \sum_i w_i = 1, \qquad w_i \geq 0
$$

**Convexidad.** La norma $\|\mathbf{w}\|_1 = \sum_i |w_i|$ es convexa (toda norma es convexa, Boyd §3.1.5). La suma ponderada con $\gamma > 0$ de dos funciones convexas es convexa. ∎

**Nota sobre no-negatividad.** Cuando ya existe la restricción $w_i \geq 0$, se tiene $\|\mathbf{w}\|_1 = \sum_i w_i = 1$ (por la restricción de presupuesto). En este caso, L₁ es **redundante** — todos los portafolios factibles tienen la misma norma L₁. Para que L₁ sea efectiva, se necesita permitir posiciones cortas o usar L₁ sobre las desviaciones respecto a un benchmark.

### Tracking error como SOCP (Boyd & Vandenberghe, 2004, §4.3.1)

Una restricción de tracking error limita la desviación del portafolio respecto a un benchmark $\mathbf{b}$. Se formula como una restricción de cono de segundo orden (SOC):

$$
\left\| \Sigma^{1/2} (\mathbf{w} - \mathbf{b}) \right\|_2 \leq \tau
$$

que es equivalente a la restricción cuadrática:

$$
(\mathbf{w} - \mathbf{b})^\top \Sigma (\mathbf{w} - \mathbf{b}) \leq \tau^2
$$

El problema completo es un **SOCP** (Second-Order Cone Program):

$$
\min_{\mathbf{w}} \quad \mathbf{w}^\top \Sigma \mathbf{w}
$$

sujeto a:

$$
\left\| \Sigma^{1/2}(\mathbf{w} - \mathbf{b}) \right\|_2 \leq \tau, \qquad \sum_i w_i = 1, \qquad w_i \geq 0
$$

**Convexidad.** El cono de segundo orden $\mathcal{K} = \{(x,t) : \|x\|_2 \leq t\}$ es un conjunto convexo (por la desigualdad triangular). La preimagen de un conjunto convexo bajo una transformación afín es convexa (Boyd §2.3.2). La intersección con las restricciones lineales preserva la convexidad. ∎

**Interpretación financiera.** La formulación SOCP es preferible a la QCQP equivalente porque los solvers SOCP (ECOS, MOSEK) explotan la estructura cónica para mayor eficiencia numérica. Además, permite agregar múltiples restricciones de tracking error simultáneamente (por ejemplo, contra diferentes benchmarks sectoriales).

---

## Estrategias de opciones

Esta clase también cubre **estrategias combinadas** de opciones (Hull, 2018, Cap. 12):

| Estrategia | Composición | Visión del mercado | Ganancia máx. | Pérdida máx. |
|-----------|-------------|-------------------|:---:|:---:|
| **Bull Call Spread** | Long call K₁ + short call K₂ | Moderadamente alcista | K₂ - K₁ - costo | Costo neto |
| **Bear Put Spread** | Long put K₂ + short put K₁ | Moderadamente bajista | K₂ - K₁ - costo | Costo neto |
| **Straddle** | Long call K + long put K | Alta volatilidad | Ilimitada | c + p |
| **Strangle** | Long call K₂ + long put K₁ | Alta volatilidad (más barato) | Ilimitada | c + p |
| **Butterfly** | Long 1 call K₁ + short 2 call K + long 1 call K₂ | Baja volatilidad | K - K₁ - costo | Costo neto |

### Convexidad de los payoffs de estrategias

La convexidad del payoff determina si se puede optimizar con herramientas convexas (Boyd §3.2.3):

- **Long call/put**: payoff convexo (max(x,0) es convexa)
- **Straddle**: payoff convexo (suma de convexas)
- **Bull/bear spread**: payoff **cóncavo** (se resta una convexa)

---

## Recursos adicionales

### Documentación

| Recurso | Descripción |
|---------|-------------|
| [CVXPY — SOCP](https://www.cvxpy.org/examples/basic/socp.html) | Ejemplo de SOCP en CVXPY |
| [Hull Cap. 12](https://www.pearson.com/) | Trading Strategies Involving Options |

### Conexión con otras clases

| Clase | Relación |
|-------|----------|
| **Clase 3** | Opciones básicas (payoff, P&L, IV) |
| **Clase 4** | Frontera eficiente estándar (sin regularización) |
| **Clase 5** | Shrinkage como regularización de Σ |
| **Clase 11** | Frontera eficiente con portfolio_func.py |
| **Clase 14** | Opciones barrera (extensión path-dependent) |

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §4.3.1 (SOCP, tracking error), §4.6 (QCQP), §6.3.1–6.3.2 (regularización L₁ y Tikhonov).
- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson. — Cap. 12: Trading Strategies Involving Options.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
- **Michaud, R. O.** (1989). The Markowitz Optimization Enigma. *Financial Analysts Journal*, 45(1), 31–42.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.

---

## Navegación del curso

← **Anterior**: Clase 11: Frontera eficiente con CVXPY
→ **Siguiente**: Clase 13: Portafolio con bono (MC vs Markowitz)

---

*Archivo de apoyo para la Clase 12 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
