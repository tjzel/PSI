import numpy as np

sample = np.random.uniform(size=10000)

parameters = [
    {"mu": 0, "sigma": 1},
    {"mu": 0, "sigma": 2},
    {"mu": 1, "sigma": 1},
    {"mu": 0.5, "sigma": 0.2},
]


# split normal distribution pdf
def Gpdf(x, mu, sigma):
    return (
        1 / (sigma * (2 * np.pi) ** 0.5) * np.e ** (-((x - mu) ** 2) / (2 * sigma**2))
    )


def log_likelihood(data, mu, sigma):
    return np.sum(np.log(Gpdf(data, mu, sigma)))


for param in parameters:
    mu, sigma = param["mu"], param["sigma"]
    print(
        f"mu: {mu}, sigma: {sigma}, log likelihood: {log_likelihood(sample, mu, sigma)}"
    )
