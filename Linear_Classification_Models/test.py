from Linear_Classification_Models.data_generation import generate_linear, generate_polynomial
from Linear_Classification_Models.Linear_Regression import linear_regression
import matplotlib.pyplot as plt
import numpy as np

X, y = generate_linear()

betas = linear_regression(X,y)

plt.scatter(X[0,np.where(y == 1)],X[1, np.where(y == 1)], color='b')
plt.scatter(X[0,np.where(y == -1)],X[1, np.where(y == -1)], color='r')

a = np.linspace(0,20, 1000)
b = betas[0] + a*betas[1]

plt.plot(a,b)