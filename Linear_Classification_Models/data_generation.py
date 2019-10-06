import numpy as np


def generate_data():
    a = np.random.multivariate_normal([5,5], [[1,0],[0,1]], 100).T
    a = np.append(a, np.ones((1,a.shape[1])), axis=0)

    b = np.random.multivariate_normal([10,10], [[1,0],[0,1]], 100).T
    b = np.append(b, -np.ones((1,b.shape[1])), axis=0)

    c = np.concatenate((a, b), axis=1)

    return c[0:2].reshape(c.shape[1], 2), c[2].reshape(c.shape[1], 1)


def generate_linear(intercept=False):

    x = np.linspace(1,10,100)
    error = np.random.uniform(-0.2,0.2,100)
    y = 1 + 0.1 * x + error

    x = x.reshape(100,1)
    y = y.reshape(100,1)

    if intercept:
        x = np.hstack((np.ones(100).reshape(100,1), x))

    return x, y


def generate_polynomial(intercept=False, p=1):

    x = np.linspace(1,10,100)
    error = np.random.uniform(-0.2,0.2,100)
    y = 1 + 0.1 * x + error

    x = x.reshape(100,1)
    y = y.reshape(100,1)

    if intercept:
        x = np.hstack((np.ones(100).reshape(100,1), x))

    return x, y