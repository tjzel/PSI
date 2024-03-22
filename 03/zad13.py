import numpy as np
from scipy.stats import multivariate_normal

# Parametry rozkładu wielowymiarowego
mean = [0, 0]
cov = [[1, 0], [0, 1]]

# 1. Wylosowanie próbki z rozkładu wielowymiarowego korzystając z scipy.stats.multivariate_normal
sample_scipy = multivariate_normal.rvs(mean=mean, cov=cov, size=100)

# 2. Wylosowanie próbki z rozkładu wielowymiarowego korzystając z numpy.random.multivariate_normal
sample_numpy = np.random.multivariate_normal(mean, cov, size=100)

print(sample_scipy)
print(sample_numpy)
