import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import seaborn as sns
from scipy import optimize

# Parametry rozkładu jednostajnego
a, b = -2, 4  # zakładamy, że chcemy losować z przedziału [-2, 4]

# Parametry rozkładu normalnego
mu, sigma = 1, 1

# Liczba próbek
N = 10000

# Losowanie próbki z rozkładu jednostajnego
uniform_data = np.random.uniform(a, b, N)

# Punkty, dla których będziemy rysować funkcję gęstości rozkładu normalnego
t = np.linspace(-3, 5, 1000)

# Rysowanie histogramu próbki z rozkładu jednostajnego
plt.hist(
    uniform_data,
    bins=100,
    density=True,
    alpha=0.6,
    color="g",
    label="Histogram próbki jednostajnej",
)

# # Rysowanie funkcji gęstości rozkładu normalnego
# plt.plot(
#     t,
#     stats.norm.pdf(t, mu, sigma),
#     "k-",
#     lw=2,
#     label="Rozkład normalny ($\mu=1$, $\sigma=1$)",
# )

# # Dodanie legendy i tytułu
# plt.legend()
# plt.title("Porównanie próbki jednostajnej i rozkładu normalnego")
# plt.show()

# Obliczenie średniej próbki
mean = np.mean(uniform_data)
# Obliczenie wariancji próbki
variance = np.var(uniform_data)
# Obliczenie odchylenia standardowego próbki
std_dev = np.sqrt(variance)
# Rysowanie funkcji gęstości rozkładu normalnego z obliczonymi parametrami
plt.plot(
    t,
    stats.norm.pdf(t, mean, std_dev),
    lw=2,
    label="Rozkład normalny (obliczone parametry)",
)

plt.show()
