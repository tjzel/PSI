import numpy as np
import scipy.stats as st
import sklearn.linear_model as lm
import matplotlib.pyplot as plt

x = np.array([0.2, 0.5, 0.8, 0.9, 1.3, 1.7, 2.1, 2.7])
deg = 1
A = np.vander(x, deg + 1)

f = lambda x: (x**2)
y = f(x) + np.random.randn(len(x))


# Solve A^t A x = A^t y
p = np.linalg.solve(np.dot(A.T, A), np.dot(A.T, y))

print(p)
