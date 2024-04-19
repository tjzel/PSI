import numpy as np
import pandas as pd
import scipy.stats as stats
import sklearn.linear_model as lm
from sklearn import datasets, linear_model
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

f = lambda x: ((x * 2 - 1) * (x**2 - 2) * (x - 2) + 3)
x_tr = np.linspace(0, 3, 200)
y_tr = f(x_tr)
# plt.figure(figsize=(6, 6))
# axes = plt.gca()
# axes.set_xlim([0, 3])
# axes.set_ylim([0, 8])
# plt.plot(x_tr[:200], y_tr[:200], "--k")
# plt.show()

x = stats.uniform(0, 3).rvs(100)
y = f(x) + stats.norm(0, 0.2).rvs(len(x))
# plt.figure(figsize=(6, 6))
# axes = plt.gca()
# axes.set_xlim([0, 3])
# axes.set_ylim([0, 8])
# plt.plot(x_tr, y_tr, "--k")
# plt.plot(x, y, "ok", ms=10)
# plt.show()

x = np.vstack(x)
# model1 = linear_model.LinearRegression()
# model1.fit(x, y)

# print(model1.coef_)
# print(model1.intercept_)
# print(model1.score(x, y))

# plt.figure(figsize=(6, 6))
# axes = plt.gca()
# axes.set_xlim([0, 3])
# axes.set_ylim([0, 8])
# plt.scatter(x, y, color="black")
# plt.plot(x, model1.predict(x), color="blue", linewidth=3)
# plt.show()

model2 = make_pipeline(PolynomialFeatures(2), linear_model.LinearRegression())
model2.fit(x, y)

# Plot outputs
plt.figure(figsize=(6, 6))
axes = plt.gca()
axes.set_xlim([0, 3])
axes.set_ylim([0, 8])
plt.scatter(x, y, color="black")
x_plot = np.vstack(np.linspace(0, 10, 100))
plt.plot(x_plot, model2.predict(x_plot), color="blue", linewidth=3)
plt.show()
