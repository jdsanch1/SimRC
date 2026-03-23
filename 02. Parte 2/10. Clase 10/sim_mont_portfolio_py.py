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
