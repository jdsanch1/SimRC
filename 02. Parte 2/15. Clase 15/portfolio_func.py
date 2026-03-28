"""
portfolio_func.py — Funciones reutilizables para optimización de portafolios.

Curso: Simulación de Riesgos y Coberturas (SimRC)
Profesor: Juan Diego Sánchez Torres — MAF ITESO

Este módulo implementa:
  - Descarga de datos con yfinance
  - Rendimientos logarítmicos
  - Simulación Monte Carlo de portafolios (estimadores robustos)
  - Frontera eficiente con CVXPY (Programación Convexa Disciplinada)
  - Frontera eficiente con bono (activo libre de riesgo)

Estimadores robustos utilizados:
  - Media: Huber (statsmodels.robust.scale.Huber)
  - Covarianza: ShrunkCovariance (sklearn.covariance)

Referencias:
  - Boyd, S. & Vandenberghe, L. (2004). Convex Optimization. §4.4 (QP).
  - Charnes, A. & Cooper, W. W. (1962). Naval Research Logistics, 9(3–4).
  - Ledoit, O. & Wolf, M. (2004). J. Multivariate Analysis, 88(2), 365–411.
  - Markowitz, H. (1952). Portfolio Selection. J. Finance, 7(1), 77–91.
"""

import numpy as np
import pandas as pd
import cvxpy as cp
import sklearn.covariance as skcov
import statsmodels.api as sm


def get_historical_closes(tickers, start_date, end_date):
    """Descarga precios de cierre ajustados usando yfinance.

    Parameters
    ----------
    tickers : str or list of str
        Ticker(s) de Yahoo Finance (e.g., 'AAPL' o ['AAPL', 'MSFT']).
    start_date : str
        Fecha de inicio en formato 'YYYY-MM-DD'.
    end_date : str
        Fecha de fin en formato 'YYYY-MM-DD'.

    Returns
    -------
    pd.DataFrame
        Precios de cierre ajustados, indexados por fecha.
    """
    import yfinance as yf

    data = yf.download(tickers, start=start_date, end=end_date,
                       auto_adjust=True, progress=False)
    if isinstance(data.columns, pd.MultiIndex):
        closes = data["Close"]
    else:
        closes = data[["Close"]]
        closes.columns = [tickers] if isinstance(tickers, str) else list(tickers)
    closes.index.name = "Date"
    return closes.dropna()


def calc_daily_returns(closes):
    """Calcula rendimientos logarítmicos diarios.

    Parameters
    ----------
    closes : pd.DataFrame
        Precios de cierre ajustados.

    Returns
    -------
    pd.DataFrame
        Rendimientos log: r_t = ln(S_t / S_{t-1}).
    """
    return np.log(closes / closes.shift(1)).iloc[1:]


def sim_mont_portfolio(daily_returns, num_portfolios, risk_free):
    """Simulación Monte Carlo de portafolios con estimadores robustos.

    Genera num_portfolios portafolios aleatorios y calcula rendimiento,
    riesgo y ratio de Sharpe anualizados usando:
      - Media robusta: estimador de Huber
      - Covarianza robusta: ShrunkCovariance (Ledoit-Wolf)

    Parameters
    ----------
    daily_returns : pd.DataFrame
        Rendimientos logarítmicos diarios (T × n).
    num_portfolios : int
        Número de portafolios aleatorios a generar.
    risk_free : float
        Tasa libre de riesgo (anualizada).

    Returns
    -------
    pd.DataFrame
        Columnas: ['Returns', 'SD', 'Sharpe', asset_1, ..., asset_n].
    """
    num_assets = daily_returns.shape[1]

    # Estimadores robustos
    huber = sm.robust.scale.Huber()
    returns_av, _ = huber(daily_returns)
    covariance = skcov.ShrunkCovariance().fit(daily_returns).covariance_

    # Pesos aleatorios normalizados (simplex)
    weights = np.random.dirichlet(np.ones(num_assets), num_portfolios)

    # Rendimiento anualizado: 252 * w'μ
    ret = 252 * weights @ returns_av

    # Riesgo anualizado: sqrt(252 * w'Σw) — vectorizado
    sd = np.sqrt(252 * np.einsum('ij,jk,ik->i', weights, covariance, weights))

    # Ratio de Sharpe
    sharpe = (ret - risk_free) / sd

    return pd.DataFrame(
        data=np.column_stack((ret, sd, sharpe, weights)),
        columns=['Returns', 'SD', 'Sharpe'] + list(daily_returns.columns)
    )


def optimal_portfolio(daily_returns, N, r):
    """Frontera eficiente mediante programación cuadrática con CVXPY (DCP).

    Resuelve N problemas paramétricos variando la aversión al riesgo μ:

        minimizar   μ · w'Σw − μ̄'w
        sujeto a    Σ wᵢ = 1,  wᵢ ≥ 0

    donde Σ es la covarianza robusta (ShrunkCovariance) y μ̄ es la media
    robusta (Huber). Ver Boyd & Vandenberghe (2004), §4.4 y §4.7.3.

    Parameters
    ----------
    daily_returns : pd.DataFrame
        Rendimientos logarítmicos diarios (T × n).
    N : int
        Número de puntos en la frontera eficiente.
    r : float
        Tasa libre de riesgo (anualizada) para el cálculo de Sharpe.

    Returns
    -------
    pd.DataFrame
        Columnas: ['Returns', 'SD', 'Sharpe', asset_1, ..., asset_n].
    """
    n = daily_returns.shape[1]
    returns_mat = np.asarray(daily_returns)

    # Estimadores robustos
    huber = sm.robust.scale.Huber()
    Sigma = skcov.ShrunkCovariance().fit(returns_mat).covariance_
    returns_av, _ = huber(returns_mat)
    mu_vec = np.asarray(returns_av).flatten()

    # Malla logarítmica de aversión al riesgo
    mus = [(10**(5.0 * t / N - 1.0) - 10**(-1)) for t in range(N)]

    # Problema DCP paramétrico (Boyd §4.7.3)
    w = cp.Variable(n)
    mu_param = cp.Parameter(nonneg=True)
    risk = cp.quad_form(w, Sigma)     # convexa (Sigma PSD)
    ret_expr = mu_vec @ w             # afín
    objective = cp.Minimize(mu_param * risk - ret_expr)
    constraints = [cp.sum(w) == 1, w >= 0]
    prob = cp.Problem(objective, constraints)

    portfolios = []
    for mu in mus:
        mu_param.value = mu
        prob.solve(solver=cp.ECOS, warm_start=True)
        if w.value is not None:
            portfolios.append(w.value.copy())

    portfolios = np.array(portfolios)
    port_returns = 252 * portfolios @ mu_vec
    port_risks = np.sqrt(252 * np.einsum('ij,jk,ik->i', portfolios, Sigma, portfolios))
    sharpe = (port_returns - r) / port_risks

    return pd.DataFrame(
        data=np.column_stack((port_returns, port_risks, sharpe, portfolios)),
        columns=['Returns', 'SD', 'Sharpe'] + list(daily_returns.columns)
    )


def optimal_portfolio_b(daily_returns, N, r, c0):
    """Frontera eficiente con bono (activo libre de riesgo) usando CVXPY (DCP).

    Extiende la matriz de covarianza con una fila/columna de ceros para el
    bono y resuelve el mismo QP paramétrico que optimal_portfolio().

    Parameters
    ----------
    daily_returns : pd.DataFrame
        Rendimientos logarítmicos diarios de activos riesgosos (T × n).
    N : int
        Número de puntos en la frontera.
    r : float
        Tasa libre de riesgo (anualizada) para Sharpe.
    c0 : float
        Rendimiento diario del bono.

    Returns
    -------
    pd.DataFrame
        Columnas: ['Returns', 'SD', 'Sharpe', asset_1, ..., asset_n, 'BOND'].
    """
    n_stocks = daily_returns.shape[1]
    n = n_stocks + 1

    # Estimadores robustos (solo acciones)
    huber = sm.robust.scale.Huber()
    Sigma_stocks = skcov.ShrunkCovariance().fit(daily_returns).covariance_
    returns_av, _ = huber(daily_returns)

    # Extender covarianza con bono (varianza = 0, covarianza = 0)
    Sigma = np.zeros((n, n))
    Sigma[:n_stocks, :n_stocks] = Sigma_stocks

    # Rendimientos esperados incluyendo bono
    mu_vec = np.append(np.asarray(returns_av).flatten(), c0)

    # Añadir columna BOND al DataFrame para nombres de columnas
    daily_returns = daily_returns.copy()
    daily_returns['BOND'] = c0

    # Malla logarítmica de aversión al riesgo
    mus = [(10**(5.0 * t / N - 1.0) - 10**(-1)) for t in range(N)]

    # Problema DCP paramétrico
    w = cp.Variable(n)
    mu_param = cp.Parameter(nonneg=True)
    risk = cp.quad_form(w, Sigma)
    ret_expr = mu_vec @ w
    objective = cp.Minimize(mu_param * risk - ret_expr)
    constraints = [cp.sum(w) == 1, w >= 0]
    prob = cp.Problem(objective, constraints)

    portfolios = []
    for mu in mus:
        mu_param.value = mu
        prob.solve(solver=cp.ECOS, warm_start=True)
        if w.value is not None:
            portfolios.append(w.value.copy())

    portfolios = np.array(portfolios)
    port_returns = 252 * portfolios @ mu_vec
    port_risks = np.sqrt(252 * np.einsum('ij,jk,ik->i', portfolios, Sigma, portfolios))
    sharpe = (port_returns - r) / port_risks

    return pd.DataFrame(
        data=np.column_stack((port_returns, port_risks, sharpe, portfolios)),
        columns=['Returns', 'SD', 'Sharpe'] + list(daily_returns.columns)
    )
