import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definicja parametrów rozkładu
mu1 = np.array([0, 0])  # średnie dla obu wymiarów
mu2 = np.array([2, 2])  # średnie dla obu wymiarów
covariance_matrix = np.array([[1, 0.0], [0.0, 1]])  # macierz kowariancji

# Generowanie siatki punktów w dwuwymiarowym obszarze
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X
pos[:, :, 1] = Y

# Obliczanie gęstości dwuwymiarowego rozkładu normalnego dla każdego punktu siatki
Z1 = (
    0.5
    * np.exp(
        -0.5
        * np.einsum(
            "ijk,kl,ijl->ij", pos - mu1, np.linalg.inv(covariance_matrix), pos - mu1
        )
    )
    / (2 * np.pi * np.sqrt(np.linalg.det(covariance_matrix)))
)

Z2 = (
    0.5
    * np.exp(
        -0.5
        * np.einsum(
            "ijk,kl,ijl->ij", pos - mu2, np.linalg.inv(covariance_matrix), pos - mu2
        )
    )
    / (2 * np.pi * np.sqrt(np.linalg.det(covariance_matrix)))
)

# Sumowanie gęstości obu rozkładów
Z = Z1 + Z2

# Wyświetlanie powierzchniowego wykresu gęstości
fig = plt.figure()
ax = fig.add_subplot(111)
ax.contourf(X, Y, Z, cmap="viridis")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_title("Gęstość dwuwymiarowego rozkładu normalnego")
plt.show()
