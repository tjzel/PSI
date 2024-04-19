import numpy as np
import pandas as pd
import scipy.stats as stats
import sklearn.linear_model as lm
import matplotlib.pyplot as plt

f = lambda x: ((x * 2 - 1) * (x**2 - 2) * (x - 2) + 3)

x = stats.uniform(0, 3).rvs(100)
y = f(x) + stats.norm(0, 0.2).rvs(len(x))

M2 = np.vstack((np.ones_like(x), x, x**2, x**3, x**4, x**5)).T
p = np.linalg.lstsq(M2, y, rcond=None)

f_lr = (
    lambda x: p[0][5] * x**5
    + p[0][4] * x**4
    + p[0][3] * x**3
    + p[0][2] * x**2
    + p[0][1] * x
    + p[0][0]
)

x_f_lr = np.linspace(0.0, 3, 200)
y_f_lr = f_lr(x_f_lr)
plt.figure(figsize=(6, 6))
axes = plt.gca()
axes.set_xlim([0, 3])
axes.set_ylim([0, 8])
plt.plot(x_f_lr, y_f_lr, "g")
plt.plot(x, y, "ok", ms=10)
plt.show()
