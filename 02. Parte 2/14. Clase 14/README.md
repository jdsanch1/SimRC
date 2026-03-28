# Clase 14 — Opciones barrera (knock-in / knock-out)

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/02.%20Parte%202/14.%20Clase%2014/14Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=02.%20Parte%202%2F14.%20Clase%2014%2F14Class%20NB.ipynb)

---

## Objetivo

Introducir las **opciones barrera** (path-dependent) y su valuación por simulación Monte Carlo. A diferencia de las opciones europeas (Clase 3 y 8), el payoff depende de toda la trayectoria del precio, no solo del valor final.

---

## Contenido teórico

### Tipos de opciones barrera

| Tipo | Activación | Efecto |
|------|-----------|--------|
| **Knock-in** | Precio toca la barrera | La opción se **activa** |
| **Knock-out** | Precio toca la barrera | La opción se **desactiva** |
| **Up** | Barrera por encima del spot | Monitorea subidas |
| **Down** | Barrera por debajo del spot | Monitorea caídas |

### Valuación por Monte Carlo

Las opciones barrera no tienen solución analítica simple (a diferencia de Black-Scholes para europeas). Nótese que el payoff involucra composiciones de funciones (max, indicadoras); la composición $\max(f(x), 0)$ preserva la convexidad cuando $f$ es convexa (Boyd & Vandenberghe, 2004, §3.2), pero el producto con una indicadora de barrera puede romperla, lo que dificulta la optimización directa de portafolios de opciones barrera. La simulación Monte Carlo es el método estándar:

1. Generar N trayectorias completas del precio
2. Para cada trayectoria, verificar si la barrera fue tocada
3. Calcular el payoff condicional
4. Promediar y descontar

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §3.2 (operaciones que preservan convexidad), §6.1–6.2 (aproximación y calibración).
- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson. — Cap. 26: Exotic Options.
- **Glasserman, P.** (2003). *Monte Carlo Methods in Financial Engineering*. Springer. — Cap. 6: Barrier options.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning. — Cap. 8: Opciones exóticas.

---

## Navegación del curso

← **Anterior**: Clase 13: Portafolio con bono
→ **Siguiente**: Clase 15: Programación estocástica

---

*Archivo de apoyo para la Clase 14 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
