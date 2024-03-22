import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

from dcor import distance_correlation

f = lambda x: np.exp(x)
x_tr = np.linspace(-10, 10, 200)
y_tr = f(x_tr)
x = stats.uniform(0, 16).rvs(100)
y = f(x) + stats.norm(0, 0.3).rvs(len(x))

pearson = stats.pearsonr(x, y)
spearman = stats.spearmanr(x, y)
kendall = stats.kendalltau(x, y)
dcor = distance_correlation(x, y)

plt.figure(figsize=(6, 6))
axes = plt.gca()
axes.set_xlim([-3, 3])
axes.set_ylim([0, 10])
# axes.set_ylim([np.min(y),f(5)])
plt.plot(x_tr, y_tr, "--k")
plt.plot(x, y, "ok", ms=3)
plt.show()

print(
    f"Pearson: {pearson}\nSpearman: {spearman}\nKendall: {kendall}\nDistance correlation: {dcor}"
)
