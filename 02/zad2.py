import numpy as np

numberOfDimensions = 5
numberOfVectors = 100

points = np.random.multivariate_normal(
    mean=np.zeros(numberOfDimensions),
    cov=np.eye(numberOfDimensions, numberOfDimensions),
    size=numberOfVectors,
)

means = np.mean(points, axis=0)
stds = np.std(points, axis=0)

normalizedPoints = (points - means) / stds

# one-liner

normalizedPoints = (points - np.mean(points, axis=0)) / np.std(points, axis=0)

print(np.mean(normalizedPoints))

covarianceMatrix = np.cov(normalizedPoints, rowvar=False)

print(covarianceMatrix)
