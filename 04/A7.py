import numpy as np
import matplotlib.pyplot as plt


def splitGaussian(x, mu, variance, tausqr):
    c = np.sqrt(2 / np.pi) / np.sqrt(variance) / (1 + np.sqrt(tausqr))
    if x <= mu:
        return c * np.exp(-((x - mu) ** 2) / (2 * variance))
    else:
        return c * np.exp(-((x - mu) ** 2) / (2 * variance * tausqr))


def log_likelihood(data, mu, sigma, tau):
    return np.sum(np.log(splitGaussian(data, mu, sigma, tau)))
