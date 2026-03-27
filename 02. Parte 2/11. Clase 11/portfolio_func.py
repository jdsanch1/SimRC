
def get_historical_closes(tickers, start_date, end_date):
    """Descarga precios de cierre ajustados usando yfinance."""
    import yfinance as yf
    import pandas as pd
    data = yf.download(tickers, start=start_date, end=end_date,
                       auto_adjust=True, progress=False)
    if isinstance(data.columns, pd.MultiIndex):
        closes = data["Close"]
    else:
        closes = data[["Close"]]
        closes.columns = [tickers] if isinstance(tickers, str) else list(tickers)
    closes.index.name = "Date"
    return closes.dropna()

def sim_mont_portfolio(daily_returns,num_portfolios,risk_free):
    num_assets=len(daily_returns.T)
    #Packages
    import pandas as pd
    import sklearn.covariance as skcov
    import numpy as np
    import statsmodels.api as sm
    huber = sm.robust.scale.Huber()
    #Mean and standar deviation returns
    returns_av, scale = huber(daily_returns)
    #returns_av = daily_returns.mean()
    covariance= skcov.ShrunkCovariance().fit(daily_returns).covariance_
    #Simulated weights
    weights = np.array(np.random.random(num_assets*num_portfolios)).reshape(num_portfolios,num_assets)
    weights = weights / weights.sum(axis=1, keepdims=True)
    ret=252*weights.dot(returns_av).T
    sd = np.zeros(num_portfolios)
    for i in range(num_portfolios):
        sd[i]=np.sqrt(252*(((weights[i,:]).dot(covariance)).dot(weights[i,:].T)))
    sharpe=np.divide((ret-risk_free),sd)
    return pd.DataFrame(data=np.column_stack((ret,sd,sharpe,weights)),columns=(['Returns','SD','Sharpe']+list(daily_returns.columns)))

def calc_daily_returns(closes):
    import numpy as np
    return np.log(closes/closes.shift(1))[1:]

def optimal_portfolio(daily_returns, N, r):
    """Frontera eficiente mediante programación cuadrática con CVXPY (DCP).

    Resuelve N problemas paramétricos:
        minimizar   μ · w'Σw − μ̄'w
        sujeto a    Σ wᵢ = 1,  wᵢ ≥ 0

    donde μ recorre una malla logarítmica de aversión al riesgo.
    """
    import pandas as pd
    import sklearn.covariance as skcov
    import numpy as np
    import cvxpy as cp
    import statsmodels.api as sm

    huber = sm.robust.scale.Huber()
    n = len(daily_returns.T)
    returns_mat = np.asmatrix(daily_returns)

    # Estimadores robustos
    Sigma = skcov.ShrunkCovariance().fit(returns_mat).covariance_
    returns_av, _ = huber(returns_mat)
    mu_vec = np.asarray(returns_av).flatten()

    # Malla de aversión al riesgo (misma que la versión original)
    mus = [(10**(5.0 * t/N - 1.0) - 10**(-1)) for t in range(N)]

    # Problema DCP paramétrico
    w = cp.Variable(n)
    mu_param = cp.Parameter(nonneg=True)
    risk = cp.quad_form(w, Sigma)       # convexa (Sigma PSD)
    ret_expr = mu_vec @ w               # afín
    objective = cp.Minimize(mu_param * risk - ret_expr)
    constraints = [cp.sum(w) == 1, w >= 0]
    prob = cp.Problem(objective, constraints)

    portfolios = []
    for mu in mus:
        mu_param.value = mu
        prob.solve(solver=cp.ECOS, warm_start=True)
        portfolios.append(w.value.copy())

    portfolios = np.array(portfolios)
    port_returns = 252 * portfolios @ mu_vec
    port_risks = np.array([np.sqrt(252 * p @ Sigma @ p) for p in portfolios])
    sharpe = (port_returns - r) / port_risks

    return pd.DataFrame(
        data=np.column_stack((port_returns, port_risks, sharpe, portfolios)),
        columns=['Returns', 'SD', 'Sharpe'] + list(daily_returns.columns)
    )

def optimal_portfolio_b(daily_returns, N, r, c0):
    """Frontera eficiente con bono (activo libre de riesgo) usando CVXPY (DCP).

    Extiende la matriz de covarianza con una fila/columna de ceros para el bono
    y resuelve el mismo QP paramétrico.
    """
    import pandas as pd
    import sklearn.covariance as skcov
    import numpy as np
    import cvxpy as cp
    import statsmodels.api as sm

    huber = sm.robust.scale.Huber()

    # Extender covarianza con bono (varianza = 0)
    Sigma_stocks = skcov.ShrunkCovariance().fit(daily_returns).covariance_
    n_stocks = len(daily_returns.T)
    n = n_stocks + 1
    Sigma = np.zeros((n, n))
    Sigma[:n_stocks, :n_stocks] = Sigma_stocks

    # Rendimientos esperados incluyendo bono
    returns_av, _ = huber(daily_returns)
    mu_vec = np.append(np.asarray(returns_av).flatten(), c0)

    # Añadir columna BOND al DataFrame
    daily_returns = daily_returns.copy()
    daily_returns['BOND'] = c0 * np.ones(daily_returns.index.size)

    # Malla de aversión al riesgo
    mus = [(10**(5.0 * t/N - 1.0) - 10**(-1)) for t in range(N)]

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
        portfolios.append(w.value.copy())

    portfolios = np.array(portfolios)
    port_returns = 252 * portfolios @ mu_vec
    port_risks = np.array([np.sqrt(252 * p @ Sigma @ p) for p in portfolios])
    sharpe = (port_returns - r) / port_risks

    return pd.DataFrame(
        data=np.column_stack((port_returns, port_risks, sharpe, portfolios)),
        columns=['Returns', 'SD', 'Sharpe'] + list(daily_returns.columns)
    )
