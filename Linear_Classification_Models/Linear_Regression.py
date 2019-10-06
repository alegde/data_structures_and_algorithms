import numpy as np
import matplotlib.pyplot as plt
from Linear_Classification_Models.data_generation import generate_data


def linear_regression(X, y, l):
    B = np.dot(np.dot(np.linalg.inv(np.dot(X.T, X) + l * np.identity(X.shape[1])), X.T), y)
    return B


def kernel_regression(X, y):
    pass

