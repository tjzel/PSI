import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt

# Set a seed for your random number generator
np.random.seed(0)

sample = np.random.uniform(size=10000)


def splitGaussian(x, m, sigma_sq, tau_sq):
    c = np.sqrt(2 / np.pi) / np.sqrt(sigma_sq) / (1 + np.sqrt(tau_sq))

    pdf = np.zeros_like(x)
    pdf[x <= m] = c * np.exp(-0.5 * (x[x <= m] - m) ** 2 / sigma_sq)
    pdf[x > m] = c * np.exp(-0.5 * (x[x > m] - m) ** 2 / (tau_sq * sigma_sq))

    return pdf


def log_likelihood(data, mu, sigma, tau):
    constant = 1e-10  # a small value to avoid log(0)
    return np.sum(np.log(splitGaussian(data, mu, sigma**2, tau**2) + constant))


def objective(params):
    mu, sigma, tau = params
    return -log_likelihood(sample, mu, sigma, tau)


initial_params = [0.5, 0.2, 0.01]

# Define the bounds for each parameter: mu can vary from -Inf to Inf, sigma from a small positive
# number very close to zero to Inf, and similarly for tau.

epsilon = 1e-5
bounds = [(None, None), (epsilon, None), (epsilon, None)]

res = optimize.minimize(objective, initial_params, bounds=bounds)

optimized_params = res.x

print("Optimized Parameters:")
print("mu =", optimized_params[0])
print("sigma =", optimized_params[1])
print("tau =", optimized_params[2])


# Generate x values for plotting
x = np.linspace(-2, 2, 1000)

# Calculate the split Gaussian PDF using the optimized parameters
pdf = splitGaussian(
    x, optimized_params[0], optimized_params[1] ** 2, optimized_params[2] ** 2
)

# Plot the histogram of the data
plt.hist(sample, bins=50, density=True, alpha=0.5, label="Data")

# Plot the split Gaussian distribution
plt.plot(x, pdf, label="Split Gaussian Distribution")

plt.xlabel("x")
plt.ylabel("Probability Density")
plt.title("Split Gaussian Distribution")
plt.legend()
plt.show()
