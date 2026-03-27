# Clase 3 — Opciones financieras: payoff, P&L y volatilidad implícita

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/jdsanch1/simrc/blob/master/01.%20Parte%201/03.%20Clase%203/03Class%20NB.ipynb)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/jdsanch1/SimRC/master?labpath=01.%20Parte%201%2F03.%20Clase%203%2F03Class%20NB.ipynb)

---

## Objetivo

Introducir los conceptos fundamentales de opciones financieras: tipos de contrato, payoff, ganancia y pérdida (P&L), volatilidad implícita, volatility smile/skew y paridad put-call. Se trabaja con datos reales de cadenas de opciones descargadas con `yfinance`.

---

## 1. Opciones financieras

### Definición

Una **opción** es un contrato derivado que otorga al comprador el *derecho* (no la obligación) de comprar o vender un activo subyacente a un precio predeterminado (**strike**, $K$) en o antes de una fecha futura (**vencimiento**, $T$).

### Tipos de opciones

| | Call | Put |
|---|---|---|
| **Derecho** | Comprar a precio $K$ | Vender a precio $K$ |
| **Beneficia si** | $S_T > K$ (precio sube) | $S_T < K$ (precio baja) |
| **Riesgo máximo (comprador)** | Prima pagada | Prima pagada |
| **Riesgo máximo (vendedor)** | Ilimitado (call) | $K - \text{prima}$ (put) |

### Estilo de ejercicio

- **Europea**: solo se puede ejercer al vencimiento $T$.
- **Americana**: se puede ejercer en cualquier momento $t \leq T$.
- **Bermuda**: se puede ejercer en fechas específicas.

---

## 2. Payoff

El **payoff** es el valor intrínseco de la opción al vencimiento:

$$
\text{Payoff}_{\text{call}} = \max(S_T - K, \, 0) = (S_T - K)^+
$$

$$
\text{Payoff}_{\text{put}} = \max(K - S_T, \, 0) = (K - S_T)^+
$$

### Moneyness

| Estado | Call ($S_T$ vs $K$) | Put ($S_T$ vs $K$) |
|--------|:---:|:---:|
| **In-the-money (ITM)** | $S_T > K$ | $S_T < K$ |
| **At-the-money (ATM)** | $S_T \approx K$ | $S_T \approx K$ |
| **Out-of-the-money (OTM)** | $S_T < K$ | $S_T > K$ |

---

## 3. Ganancia y pérdida (P&L)

El P&L incorpora la **prima** pagada (o recibida):

### Comprador

$$
\text{P\&L}_{\text{call buyer}} = \max(S_T - K, 0) - c
$$

$$
\text{P\&L}_{\text{put buyer}} = \max(K - S_T, 0) - p
$$

### Vendedor

$$
\text{P\&L}_{\text{call seller}} = c - \max(S_T - K, 0)
$$

$$
\text{P\&L}_{\text{put seller}} = p - \max(K - S_T, 0)
$$

### Juego de suma cero

$$
\text{P\&L}_{\text{buyer}} + \text{P\&L}_{\text{seller}} = 0
$$

### Punto de equilibrio (break-even)

- **Call**: $S_T^* = K + c$ (el precio debe superar el strike más la prima)
- **Put**: $S_T^* = K - p$ (el precio debe caer por debajo del strike menos la prima)

---

## 4. Modelo de Black-Scholes-Merton

### Fórmula para call europea

$$
C = S_0 \, \Phi(d_1) - K \, e^{-rT} \, \Phi(d_2)
$$

$$
P = K \, e^{-rT} \, \Phi(-d_2) - S_0 \, \Phi(-d_1)
$$

donde:

$$
d_1 = \frac{\ln(S_0/K) + (r + \sigma^2/2)T}{\sigma\sqrt{T}}, \qquad d_2 = d_1 - \sigma\sqrt{T}
$$

- $S_0$: precio spot del subyacente
- $K$: precio strike
- $r$: tasa libre de riesgo
- $T$: tiempo al vencimiento (en años)
- $\sigma$: volatilidad del subyacente
- $\Phi$: función de distribución acumulada de la normal estándar

### Supuestos del modelo

1. El precio sigue un GBM: $dS_t = \mu S_t \, dt + \sigma S_t \, dW_t$
2. Volatilidad $\sigma$ constante
3. Tasa libre de riesgo $r$ constante
4. No hay dividendos
5. No hay costos de transacción ni impuestos
6. Es posible vender en corto

---

## 5. Volatilidad implícita

### Definición

La **volatilidad implícita** (IV) es el valor de $\sigma$ que, sustituido en la fórmula de Black-Scholes, reproduce el precio de mercado de la opción:

$$
C^{\text{mkt}} = C_{\text{BS}}(\sigma^{\text{impl}})
$$

Se obtiene invirtiendo numéricamente la fórmula (no tiene solución analítica cerrada).

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
- **Portafolio A**: una call + $K \cdot e^{-rT}$ en efectivo
- **Portafolio B**: una put + una acción

Ambos valen $\max(S_T, K)$ en $T$, por lo que deben valer lo mismo hoy (no arbitraje).

---

## 7. Las "griegas"

Las **griegas** miden la sensibilidad del precio de una opción a cambios en los parámetros:

| Griega | Símbolo | Mide sensibilidad a | Fórmula (call) |
|--------|---------|---------------------|----------------|
| **Delta** | $\Delta$ | Precio del subyacente $S$ | $\Phi(d_1)$ |
| **Gamma** | $\Gamma$ | Segunda derivada respecto a $S$ | $\frac{\phi(d_1)}{S\sigma\sqrt{T}}$ |
| **Theta** | $\Theta$ | Paso del tiempo $t$ | $-\frac{S\phi(d_1)\sigma}{2\sqrt{T}} - rKe^{-rT}\Phi(d_2)$ |
| **Vega** | $\mathcal{V}$ | Volatilidad $\sigma$ | $S\sqrt{T}\phi(d_1)$ |
| **Rho** | $\rho$ | Tasa de interés $r$ | $KTe^{-rT}\Phi(d_2)$ |

donde $\phi$ es la función de densidad de la normal estándar.

> Las griegas se explorarán en detalle en la Clase 14 (opciones barrera).

---

## Referencias bibliográficas

### Textos principales

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
    │     ├── Fórmula: C = S·Φ(d₁) - K·e^(-rT)·Φ(d₂)
    │     └── Griegas: Δ, Γ, Θ, V, ρ
    │
    ├── Volatilidad implícita
    │     ├── Inversión numérica de B-S
    │     ├── Smile / Skew
    │     └── Refleja expectativas del mercado
    │
    └── Paridad put-call
          ├── C - P = S₀ - K·e^(-rT)
          └── Condición de no arbitraje
```

---

*Archivo de apoyo para la Clase 3 del curso **Simulación de Riesgos y Coberturas** (SimRC).*
*Profesor: Juan Diego Sánchez Torres — MAF ITESO.*
