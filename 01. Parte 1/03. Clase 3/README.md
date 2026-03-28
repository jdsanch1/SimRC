# Clase 3 — Opciones financieras: payoff, P&L y volatilidad implícita

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/03.%20Clase%203/03Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F03.%20Clase%203%2F03Class%20NB.ipynb)

---

## Objetivo

Introducir los conceptos fundamentales de opciones financieras: tipos de contrato, payoff, ganancia y pérdida (P&L), volatilidad implícita, volatility smile/skew y paridad put-call. Se trabaja con datos reales de cadenas de opciones descargadas con `yfinance`.

---

## 1. Opciones financieras

### Definición

Una **opción** es un contrato derivado que otorga al comprador el *derecho* (no la obligación) de comprar o vender un activo subyacente a un precio predeterminado (el **strike** K) en o antes de una fecha futura (el **vencimiento** T).

### Tipos de opciones

| | Call | Put |
|---|---|---|
| **Derecho** | Comprar a precio K | Vender a precio K |
| **Beneficia si** | El precio sube | El precio baja |
| **Riesgo máx. (comprador)** | Prima pagada | Prima pagada |
| **Riesgo máx. (vendedor)** | Ilimitado | K menos la prima |

### Estilo de ejercicio

- **Europea**: solo se puede ejercer al vencimiento T.
- **Americana**: se puede ejercer en cualquier momento antes de T.
- **Bermuda**: se puede ejercer en fechas específicas predeterminadas.

---

## 2. Payoff

El **payoff** es el valor intrínseco de la opción al vencimiento.

**Call:**

$$
\text{Payoff} = \max(S_T - K, \ 0)
$$

**Put:**

$$
\text{Payoff} = \max(K - S_T, \ 0)
$$

Nótese que la función $\max(x, 0)$ es convexa y no decreciente (Boyd & Vandenberghe, 2004, §3.2.3), por lo que el payoff de una opción es una función convexa de $S_T$.

### Moneyness

| Estado | Call | Put |
|--------|------|-----|
| **In-the-money (ITM)** | Precio > Strike | Precio < Strike |
| **At-the-money (ATM)** | Precio ≈ Strike | Precio ≈ Strike |
| **Out-of-the-money (OTM)** | Precio < Strike | Precio > Strike |

---

## 3. Ganancia y pérdida (P&L)

El P&L incorpora la **prima** pagada o recibida.

### Comprador de call

$$
\text{PnL} = \max(S_T - K, \ 0) - c
$$

### Comprador de put

$$
\text{PnL} = \max(K - S_T, \ 0) - p
$$

### Vendedor de call

$$
\text{PnL} = c - \max(S_T - K, \ 0)
$$

### Vendedor de put

$$
\text{PnL} = p - \max(K - S_T, \ 0)
$$

### Juego de suma cero

La suma del PnL del comprador y del vendedor siempre es cero:

$$
\text{PnL}\_{\text{comprador}} + \text{PnL}\_{\text{vendedor}} = 0
$$

### Punto de equilibrio (break-even)

- **Call**: el precio debe superar K + c
- **Put**: el precio debe caer por debajo de K - p

---

## 4. Modelo de Black-Scholes-Merton

### Fórmula para call europea

$$
C = S_0 \, \Phi(d_1) - K \, e^{-rT} \, \Phi(d_2)
$$

### Fórmula para put europea

$$
P = K \, e^{-rT} \, \Phi(-d_2) - S_0 \, \Phi(-d_1)
$$

### Parámetros d1 y d2

$$
d_1 = \frac{\ln(S_0 / K) + (r + \sigma^2 / 2) \, T}{\sigma \sqrt{T}}
$$

$$
d_2 = d_1 - \sigma \sqrt{T}
$$

Donde:
- **S₀**: precio spot del subyacente
- **K**: precio strike
- **r**: tasa libre de riesgo
- **T**: tiempo al vencimiento (en años)
- **σ**: volatilidad del subyacente
- **Φ**: función de distribución acumulada de la normal estándar

### Supuestos del modelo

1. El precio sigue un Movimiento Browniano Geométrico (GBM)
2. Volatilidad σ constante
3. Tasa libre de riesgo r constante
4. No hay dividendos
5. No hay costos de transacción ni impuestos
6. Es posible vender en corto

---

## 5. Volatilidad implícita

### Definición

La **volatilidad implícita** (IV) es el valor de σ que, sustituido en la fórmula de Black-Scholes, reproduce el precio de mercado de la opción:

$$
C^{\text{mkt}} = C_{\text{BS}}(\sigma^{\text{impl}})
$$

Se obtiene invirtiendo numéricamente la fórmula (no tiene solución analítica cerrada). La calibración robusta de la IV puede formularse con la penalización de Huber (Boyd & Vandenberghe, 2004, §6.1.2), que modera la influencia de precios de mercado atípicos.

### Volatility smile y skew

Si el modelo Black-Scholes fuera exacto, la IV sería **constante** para todos los strikes. En la práctica:

- **Smile**: IV mínima ATM, mayor para ITM y OTM. Común en mercados de divisas.
- **Skew** (smirk): IV más alta para puts OTM que para calls OTM. Dominante en mercados de acciones post-1987.

El skew refleja:
- Mayor demanda de puts OTM como **protección** (seguro contra caídas)
- Colas pesadas en la distribución de rendimientos (leptocurtosis)
- Aversión al riesgo asimétrica

---

## 6. Paridad put-call

Para opciones europeas sobre un activo sin dividendos:

$$
C - P = S_0 - K \, e^{-rT}
$$

### Implicaciones

- Conocer el precio de la call determina el de la put (y viceversa)
- Es una condición de **no arbitraje**: si se viola, existe una estrategia de ganancia sin riesgo
- Permite verificar la consistencia de los precios de mercado

### Demostración

Se construyen dos portafolios con el mismo payoff a vencimiento:
- **Portafolio A**: una call + efectivo por valor de K · exp(-rT)
- **Portafolio B**: una put + una acción

Ambos valen max(S_T, K) en T, por lo que deben valer lo mismo hoy (no arbitraje).

---

## 7. Las "griegas"

Las **griegas** miden la sensibilidad del precio de una opción a cambios en los parámetros del modelo.

### Delta (Δ)

Sensibilidad al precio del subyacente S. Para una call:

$$
\Delta = \Phi(d_1)
$$

### Gamma (Γ)

Segunda derivada respecto a S (curvatura del delta):

$$
\Gamma = \frac{\phi(d_1)}{S \, \sigma \sqrt{T}}
$$

### Theta (Θ)

Sensibilidad al paso del tiempo (time decay):

$$
\Theta = -\frac{S \, \phi(d_1) \, \sigma}{2\sqrt{T}} - r \, K \, e^{-rT} \, \Phi(d_2)
$$

### Vega (ν)

Sensibilidad a la volatilidad σ:

$$
\nu = S \sqrt{T} \, \phi(d_1)
$$

### Rho (ρ)

Sensibilidad a la tasa de interés r:

$$
\rho = K \, T \, e^{-rT} \, \Phi(d_2)
$$

En estas fórmulas, φ denota la función de densidad de la normal estándar.

> Las griegas se explorarán en detalle en la Clase 14 (opciones barrera).

---

## Referencias bibliográficas

### Textos principales

- **Boyd, S. & Vandenberghe, L.** (2004). *Convex Optimization*. Cambridge University Press. — §3.2.3 (convexidad de payoffs), §4.3.2 (SOCP), §6.1.2 (penalización de Huber).

- **Hull, J. C.** (2018). *Options, Futures, and Other Derivatives* (10th ed.). Pearson.
  - Cap. 1: Introduction. Cap. 10–11: Mechanics of Options, Properties of Stock Options.
  - Cap. 15: The Black-Scholes-Merton Model. Cap. 20: Volatility Smiles.
- **Luenberger, D. G.** (2013). *Investment Science* (2nd ed.). Oxford University Press.
  - Cap. 12–13: Basic Options Theory.
- **Venegas Martínez, F.** (2008). *Riesgos financieros y económicos* (2a ed.). Cengage Learning.
  - Cap. 5–6: Opciones, paridad put-call, modelo Black-Scholes.
- **Tsay, R. S.** (2010). *Analysis of Financial Time Series* (3rd ed.). Wiley.

### Artículos seminales

- **Black, F. & Scholes, M.** (1973). The Pricing of Options and Corporate Liabilities. *Journal of Political Economy*, 81(3), 637–654.
- **Merton, R. C.** (1973). Theory of Rational Option Pricing. *The Bell Journal of Economics*, 4(1), 141–183.
- **Cont, R.** (2001). Empirical Properties of Asset Returns. *Quantitative Finance*, 1(2), 223–236.

---

## Recursos adicionales

### Documentación

| Recurso | Descripción |
|---------|-------------|
| `yf.Ticker("AAPL").option_chain()` | Cadena de opciones en tiempo real |
| [CBOE](https://www.cboe.com/) | Chicago Board Options Exchange — datos y educación |
| [Options Clearing Corporation](https://www.theocc.com/) | Especificaciones de contratos |

### Conexión con otras clases

| Clase | Relación |
|-------|----------|
| **Clase 1–2** | Rendimientos y covarianza del subyacente |
| **Clase 7** | Análisis de riesgo (VaR) que motiva la cobertura con opciones |
| **Clase 14** | Opciones barrera (knock-in/knock-out) — extensiones path-dependent |

---

## Mapa conceptual de la Clase 3

```
Opciones financieras
    │
    ├── Tipos: Call / Put
    │     ├── Europea / Americana / Bermuda
    │     └── Comprador (holder) / Vendedor (writer)
    │
    ├── Payoff
    │     ├── Call: max(S_T - K, 0)
    │     ├── Put:  max(K - S_T, 0)
    │     └── Moneyness: ITM / ATM / OTM
    │
    ├── P&L = Payoff ± Prima
    │     ├── Comprador: payoff - prima
    │     ├── Vendedor: prima - payoff
    │     └── Suma cero
    │
    ├── Black-Scholes-Merton
    │     ├── Supuestos: GBM, σ constante
    │     ├── C = S·Φ(d₁) - K·exp(-rT)·Φ(d₂)
    │     └── Griegas: Δ, Γ, Θ, ν, ρ
    │
    ├── Volatilidad implícita
    │     ├── Inversión numérica de B-S
    │     ├── Smile / Skew
    │     └── Refleja expectativas del mercado
    │
    └── Paridad put-call
          ├── C - P = S₀ - K·exp(-rT)
          └── Condición de no arbitraje
```

---


## Navegación del curso

← **Anterior**: Clase 2: Retornos y covarianza  
→ **Siguiente**: Clase 4: Ratio de Sharpe y portafolio óptimo

---

*Archivo de apoyo para la Clase 3 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
