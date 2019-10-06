import numpy as np
from numerical_algorithms.equiations_one_variable.utils import linear, quadratic, linear_loss, quadratic_loss


def bisection(my_function, a, b, tol, N):
    """
    Finds the solution to the equation f(x) = 0
    :param function: Function to be solved for.
    :param range: Initial range in which the minimum is thought to be.
    :param tol: Limit for which to stop looking.
    :param N: Maximum number of iterations.
    :return: Value x at which the function f(x) is minimized in the selected range.
    """

    i = 0
    Fa = my_function(a)

    while i <= N:

        p = a + (b - a) / 2
        Fp = my_function(p)

        if Fp == 0 or (b - a) / 2 < tol:
            return p, i, a, b
        i += 1
        if Fa * Fp > 0:
            a = p
            Fa = Fp
        else:
            b = p

    return p


def main():

    global x, y

    N = 100
    beta = 1
    x = np.linspace(0,10,N)
    noise = np.random.normal(0,1,N)
    y = linear(x, beta) + noise

    result = bisection(linear_loss, -10, 10, 0.000001, 100)

    return result


