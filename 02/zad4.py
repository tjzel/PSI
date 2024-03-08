import numpy as np
from sklearn.datasets import load_breast_cancer

X, y = load_breast_cancer(return_X_y=True)

# print(X)
# print(y)

renumeratedY = np.where(y == 0, -1, +1)

minX = np.min(X, axis=0)
print(minX)

maxX = np.max(X, axis=0)
print(maxX)

rescaledX = (X - minX) / (maxX - minX)

print(rescaledX)
print(renumeratedY)
