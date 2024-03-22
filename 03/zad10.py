import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Definicja parametrów rozkładu
mu = np.array([0, 0])  # średnie dla obu wymiarów
covariance_matrix = np.array([[1, 0.0], [0.0, 1]])  # macierz kowariancji

# Generowanie siatki punktów w dwuwymiarowym obszarze
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
pos = np.empty(X.shape + (2,))
pos[:, :, 0] = X
pos[:, :, 1] = Y

# Obliczanie gęstości dwuwymiarowego rozkładu normalnego dla każdego punktu siatki
Z = np.exp(
    -0.5
    * np.einsum("ijk,kl,ijl->ij", pos - mu, np.linalg.inv(covariance_matrix), pos - mu)
) / (2 * np.pi * np.sqrt(np.linalg.det(covariance_matrix)))

# Wyświetlanie powierzchniowego wykresu gęstości
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
ax.plot_surface(X, Y, Z, cmap="viridis")
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Gęstość")
ax.set_title("Gęstość dwuwymiarowego rozkładu normalnego")
plt.show()
