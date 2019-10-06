import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt


def nextH(H, P, b, s):

    return b*H - s*H*P


def nextP(H, P, d, e, s):
    return -d*P + e*s*H*P


def next(X, t=0):

    return np.array([1*X[0] - 0.1*X[0]*X[1],
                    -1.5 * X[1] + 0.75 * 0.1 * X[0] * X[1]])


def main(Ho, Po, s, b, d, e, iterations):

    # H = np.zeros(iterations)
    # P = np.zeros(iterations)
    #
    # H[0] = Ho
    # P[0] = Po
    #
    # for i in range(1, iterations):
    #     H[i] = H[i-1] + nextH(H[i-1], P[i-1], b, s)
    #     P[i] = P[i-1] + nextP(H[i-1], P[i-1], d, e, s)

    # return H, P

    t = np.linspace(0,15,1000)

    X0 = np.array([Ho, Po])

    X = integrate.odeint(next, X0, t)

    return X

result = main(10, 5, 0.1, 1, 1.5, 0.75, 100)
