# Clase 14 — Opciones barrera (knock-in / knock-out)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/14.%20Clase%2014/14Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F14.%20Clase%2014%2F14Class%20NB.ipynb)

---

## Objetivo

Introducir las **opciones barrera** como derivados path-dependent y valuarlas por simulación Monte Carlo. A diferencia de las opciones europeas (Clases 3 y 8), el payoff depende de **toda la trayectoria** del precio, no solo del valor final.

---

## Contenido teórico

### Opciones path-dependent

Las opciones europeas estándar solo dependen de S_T (precio al vencimiento). Las opciones barrera dependen de toda la trayectoria, lo que las hace **path-dependent** y más difíciles de valuar.

### Tipos de opciones barrera

| Tipo | Barrera vs. Spot | Se activa cuando | Efecto |
|------|:---:|---|---|
| **Down-and-out** | B < S₀ | min(S_t) ≤ B | Opción se **desactiva** (knockout) |
| **Down-and-in** | B < S₀ | min(S_t) ≤ B | Opción se **activa** (knockin) |
| **Up-and-out** | B > S₀ | max(S_t) ≥ B | Opción se **desactiva** |
| **Up-and-in** | B > S₀ | max(S_t) ≥ B | Opción se **activa** |

### Payoff formal

**Down-and-out call:**

$$
V_T = \max(S_T - K, 0) \cdot \mathbf{1}\!\left\{\min_{0 \leq t \leq T} S_t > B\right\}
$$

**Down-and-in call:**

$$
V_T = \max(S_T - K, 0) \cdot \mathbf{1}\!\left\{\min_{0 \leq t \leq T} S_t \leq B\right\}
$$

### Relación in + out = europeo

Para cada par (in, out) con la misma barrera, strike y vencimiento:

$$
V_{\text{in}} + V_{\text{out}} = V_{\text{europeo}}
$$

En toda trayectoria, exactamente una de las dos opciones está activa. Esto permite verificar numéricamente la implementación.

### Valuación por Monte Carlo

Las opciones barrera no tienen solución analítica simple. El método estándar es:

1. Generar N trayectorias completas del precio bajo medida risk-neutral
2. Para cada trayectoria, verificar si la barrera fue tocada
3. Calcular el payoff condicional (payoff × indicadora)
4. Promediar y descontar

### Ruptura de convexidad (Boyd & Vandenberghe, 2004, §3.2)

La función indicadora que determina si la barrera fue tocada **no es convexa**. Esto tiene consecuencias importantes:

**Operaciones que preservan convexidad (Boyd §3.2.3):**
- max(f, g) con f, g convexas → Convexa (payoff de call/put)
- Suma ponderada positiva → Convexa (portafolio de opciones long)
- Composición con función convexa no decreciente → Convexa

**Operación que rompe convexidad:**
- Producto con función indicadora → **No necesariamente convexa** (payoff de opciones barrera)

Esto explica por qué las opciones barrera no se pueden optimizar con CVXPY y requieren Monte Carlo.

### Efecto de la barrera en el precio

- Opciones **out** son siempre **más baratas** que las europeas (V_out ≤ V_europeo)
- Cuando B → 0 (down) o B → ∞ (up), la barrera nunca se toca y V_out → V_europeo
- Cuando B → S₀, casi todas las trayectorias tocan la barrera y V_out → 0
- Opciones barrera son populares porque ofrecen protección similar a menor costo

---

## Recursos adicionales

### Documentación

| Recurso | Descripción |
|---------|-------------|
| [numpy.random.randn](https://numpy.org/doc/stable/reference/random/generated/numpy.random.randn.html) | Generación de normales estándar |
| [numpy cumsum/min/max](https://numpy.org/doc/stable/reference/routines.math.html) | Operaciones a lo largo de trayectorias |

### Conexión con otras clases

| Clase | Relación |
|-------|----------|
| **Clase 3** | Opciones europeas (payoff, P&L, Black-Scholes) |
| **Clase 7** | Simulación MC de precios (3 modelos) |
| **Clase 8** | Valuación MC de opciones europeas |
| **Clase 12** | Estrategias de opciones (spreads, straddle) |
| **Clase 15** | Programación estocástica (optimización bajo incertidumbre) |

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §3.2 (preservación de convexidad).
- **Glasserman, P.** (2003). *Monte Carlo Methods in Financial Engineering*. Springer. — Cap. 6: Barrier options.
- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson. — Cap. 26: Exotic Options.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning. — Cap. 8: Opciones exóticas.

### Artículos seminales

- **Merton, R. C.** (1973). Theory of Rational Option Pricing. *The Bell Journal of Economics*, 4(1), 141–183.
- **Rubinstein, M. & Reiner, E.** (1991). Breaking Down the Barriers. *Risk*, 4(8), 28–35.

---

## Navegación del curso

← **Anterior**: Clase 13: Portafolio con bono (MC vs Markowitz)
→ **Siguiente**: Clase 15: Programación estocástica con Pyomo y CVXPY

---

*Archivo de apoyo para la Clase 14 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
