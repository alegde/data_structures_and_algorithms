import numpy as np
from scipy import stats


def bsm_call_value(S0, K, T, r, sigma):

    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S0 / K) + (r - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    value = S0 * stats.norm.cdf(d1, 0, 1) - np.exp(-r*T) * K * stats.norm.cdf(d2, 0, 1)

    return value


def bsm_vega(S0, K, T, r, sigma):

    d1 = (np.log(S0 / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    vega = S0 * stats.norm.cdf(d1, 0, 1) * np.sqrt(T)

    return vega


def bsm_implied_volatility(S0, K, T, r, C0, sigma_est, it=100):
    pass

