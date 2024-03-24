import numpy as np


# split normal distribution pdf
def Gpdf(x, mu, sigma):
    return (
        1 / (sigma * (2 * np.pi) ** 0.5) * np.e ** (-((x - mu) ** 2) / (2 * sigma**2))
    )


def log_likelihood(data, mu, sigma):
    return np.sum(np.log(Gpdf(data, mu, sigma)))
