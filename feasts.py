from statsmodels.tsa.seasonal import seasonal_decompose

def strength_season(ts, model='additive'):
    res = seasonal_decompose(x=ts, model=model)
res.plot()
