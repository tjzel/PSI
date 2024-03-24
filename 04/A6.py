import numpy as np
import matplotlib.pyplot as plt


def splitGaussian(x, mu, variance, tausqr):
    c = np.sqrt(2 / np.pi) / np.sqrt(variance) / (1 + np.sqrt(tausqr))
    if x <= mu:
        return c * np.exp(-((x - mu) ** 2) / (2 * variance))
    else:
        return c * np.exp(-((x - mu) ** 2) / (2 * variance * tausqr))


x = np.linspace(-5, 5, 1000)

# Parameters for the first density
mu1 = 0
sigma1 = 1
tau1 = 1
density1 = [splitGaussian(xi, mu1, sigma1**2, tau1**2) for xi in x]

# Parameters for the second density
mu2 = 0
sigma2 = 1
tau2 = 1 / 2
density2 = [splitGaussian(xi, mu2, sigma2**2, tau2**2) for xi in x]

# Parameters for the third density
mu3 = 1
sigma3 = 1 / 2
tau3 = 1
density3 = [splitGaussian(xi, mu3, sigma3**2, tau3**2) for xi in x]

# Plotting the densities
plt.plot(x, density1, label="mu=0, sigma=1, tau=1")
plt.plot(x, density2, label="mu=0, sigma=1, tau=1/2")
plt.plot(x, density3, label="mu=1, sigma=1/2, tau=1")
plt.xlabel("x")
plt.ylabel("Density")
plt.legend()
plt.show()
