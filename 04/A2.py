import numpy as np
from scipy.stats import norm

import matplotlib.pyplot as plt

# Generate a random sample from a uniform distribution
sample = np.random.uniform(size=10000)

plt.hist(
    sample,
    bins=50,
    density=True,
    alpha=0.6,
    color="g",
    label="Histogram próbki jednostajnej",
)

# Fit the parameters of a normal distribution to the sample
mu, sigma = norm.fit(sample)

# Generate x values for the plot
x = np.linspace(-1, 2, 100)

# Calculate the corresponding y values using the fitted parameters
y = norm.pdf(x, mu, sigma)

# Plot the probability density function of the normal distribution
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("Probability Density")
plt.title("Normal Distribution")
plt.show()
