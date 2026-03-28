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

Las opciones barrera no tienen solución analítica simple (a diferencia de Black-Scholes para europeas). La simulación Monte Carlo es el método estándar:

1. Generar N trayectorias completas del precio
2. Para cada trayectoria, verificar si la barrera fue tocada
3. Calcular el payoff condicional
4. Promediar y descontar

---

## Referencias bibliográficas

### Optimización convexa (Boyd & Vandenberghe, 2004)

- **§3.2 Operaciones que preservan convexidad** (pp. 79–93): El payoff de opciones barrera involucra composiciones de funciones (max, indicadoras, producto). Boyd muestra cuándo estas composiciones preservan la convexidad:
  - max(f(x), 0) es convexa si f es convexa
  - f(x) · I(condición) puede no ser convexa — esto explica por qué la optimización de portafolios de opciones barrera es más difícil

- **§6.1–6.2 Aproximación y ajuste** (pp. 291–303): La calibración de modelos para opciones barrera (ajustar parámetros del modelo a precios de mercado) es un problema de aproximación convexa cuando el modelo es lineal en los parámetros.

### Otros textos

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
