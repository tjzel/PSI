import matplotlib.pyplot as plt
import numpy as np
import numpy.random as rnd
import scipy.stats as stats
from scipy.stats import multivariate_normal

mean1 = np.array([0, 0])
cov1 = np.array([[4.40, -2.75], [-2.75, 5.50]])
X1_rv = multivariate_normal(mean1, cov1)
X = X1_rv.rvs(1000)

means = X.mean(axis=0)
cov = np.cov(X.T)

X2_rv = multivariate_normal(means, cov)
X2 = X2_rv.rvs(1000)

plt.scatter(X[:, 0], X[:, 1], label="Sample")
x, y = np.mgrid[-10:10:0.1, -10:10:0.1]
pos = np.dstack((x, y))
plt.contourf(x, y, X2_rv.pdf(pos), levels=10, colors="r", label="Normal Distribution")
plt.legend()
plt.show()
