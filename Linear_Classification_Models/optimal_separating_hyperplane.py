import numpy as np
from scipy.optimize import minimize, LinearConstraint
import matplotlib.pyplot as plt
from Linear_Classification_Models.data_generation import generate_data


X, y = generate_data()


def OSH(X, y):
    x0 = np.zeros(y.shape[1])
    Z = np.dot(y,y.T) * np.dot(X.T,X)
    constraint1 = LinearConstraint(x0, 0, np.inf, keep_feasible=True)
    constraint2 = LinearConstraint(y.dot(x0), 0, 0)
    result = minimize(funct, x0, args=(Z), method='trust-constr', constraints=[constraint1])


def funct(alpha, args):
    print("Step")
    #print(alpha)
    Z = args[0]

    a = 0.5 * np.dot(np.dot(np.transpose(alpha), Z), alpha) - np.sum(alpha)
    print(a)
    return a

plt.scatter(a[0],a[1], color='b')
plt.scatter(b[0],b[1], color='r')

