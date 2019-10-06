import numpy as np
import matplotlib.pyplot as plt
from pyearth import Earth
def generate_data():
    alpha1 = 0
    beta1 = 1

    n_samples = 50
    noise1 = 2*np.random.randn(n_samples)
    x1 = np.linspace(1,50,50)
    y1 = alpha1 + beta1 * x1 + noise1

    alpha2 = (alpha1 + beta1 * 50) * 2
    beta2 = -1

    n_samples = 50
    noise2 = 2*np.random.randn(n_samples)
    x2 = np.linspace(50,100,50)
    y2 = alpha2 + beta2 * x2 + noise2

    x = np.concatenate((x1,x2), axis=None)
    y = np.concatenate((y1,y2), axis=None)

    return x, y

x, y = generate_data()
mars = Earth(max_terms=2)
mars.fit(x,y)
Y_hat = mars.predict(x)
plt.scatter(x,y)
plt.scatter(x,Y_hat)
plt.show()