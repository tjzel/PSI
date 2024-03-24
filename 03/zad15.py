import numpy as np

import matplotlib.pyplot as plt

# Generowanie próbki na kwadracie [0,1] x [0,1]
np.random.seed(0)
n = 1000
x = np.random.uniform(0, 1, n)
y = np.random.uniform(0, 1, n)
sample = np.vstack((x, y)).T

# Obliczanie średniej próbki
mean = np.mean(sample, axis=0)

# Obliczanie macierzy kowariancji próbki
cov_matrix = np.cov(sample.T)

# Rysowanie wykresu
fig, ax = plt.subplots()

# Wykres próbki


# Poziomice rozkładu normalnego
x_grid, y_grid = np.meshgrid(np.linspace(-0.6, 1.6, 100), np.linspace(-0.6, 1.6, 100))
pos = np.empty(x_grid.shape + (2,))
pos[:, :, 0] = x_grid
pos[:, :, 1] = y_grid
z = np.exp(
    -0.5 * np.sum((pos - mean) @ np.linalg.inv(cov_matrix) * (pos - mean), axis=2)
)
ax.contourf(
    x_grid,
    y_grid,
    z,
    # levels=10,
    # colors="r",
    cmap="viridis",
    alpha=0.5,
    label="Poziomice rozkładu normalnego",
)

ax.scatter(x, y, label="Próbka", s=1)

# Wektory własne macierzy kowariancji
eigenvalues, eigenvectors = np.linalg.eig(cov_matrix)
for eigenvalue, eigenvector in zip(eigenvalues, eigenvectors.T):
    ax.quiver(
        mean[0],
        mean[1],
        eigenvector[0],
        eigenvector[1],
        angles="xy",
        scale_units="xy",
        scale=1,
        color="g",
        label="Wektory własne macierzy kowariancji",
    )

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.legend()

# Set the limits of x and y axes
ax.set_xlim(-0.6, 1.6)
ax.set_ylim(-0.6, 1.6)

plt.show()
