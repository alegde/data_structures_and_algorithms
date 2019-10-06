import numpy as np
from numerical_algorithms.equiations_one_variable.utils import linear, fixed_point_linear_loss


def fixed_point(my_function, p0, TOL, N):

    i = 0

    while i <= N:
        p = my_function(x, y, p0)

        if np.abs(p - p0) < TOL:
            return p

        i += 1
        p0 = p

    return p


def main():

    global x, y

    N = 100
    beta = 1
    x = np.linspace(0,10,N)
    noise = np.random.normal(0,1,N)
    y = linear(x, beta) + noise

    result = fixed_point(fixed_point_linear_loss, 10, 0.000001, 100)

    return result