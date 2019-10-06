import numpy as np


def linear(x, beta):
    return beta * x


def quadratic(x, beta):
    return beta * x ** 2


def linear_loss(x, params):
    return np.mean(y - linear(x, params))


def quadratic_loss(params):
    return np.mean(y - quadratic(x, params))


def fixed_point_linear_loss(x, y, params):
    return np.square(params) * (np.sum(x) / np.sum(y))


# def fixed_point_linear_loss(x, y, params):
#     return np.sqrt(np.sum(np.square(y) + np.square(params) * np.square(x)) / np.sum(2 * np.square(y) * np.square(x)))