import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

# function
f = lambda x: ((x * 2 - 1) * (x**2 - 2) * (x - 2) + 3)

# generating data
x = stats.uniform(0, 3).rvs(100)
y = f(x) + stats.norm(0, 0.2).rvs(len(x))

plt.figure(figsize=(6, 6))
axes = plt.gca()
axes.set_xlim([0, 3])
axes.set_ylim([0, 8])
plt.plot(x, y, "ok", ms=10)

# for each degree from 3 to 5
for degree in range(3, 6):
    M = np.vstack([x**i for i in range(degree + 1)]).T
    p, _, _, _ = np.linalg.lstsq(M, y, rcond=None)

    f_lr = lambda x: sum([p[i] * x**i for i in range(degree + 1)])
    x_f_lr = np.linspace(0.0, 3, 200)
    y_f_lr = f_lr(x_f_lr)
    plt.plot(x_f_lr, y_f_lr, label=f"degree {degree}")

plt.legend()
plt.show()
