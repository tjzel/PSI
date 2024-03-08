import numpy as np

numberOfDimensions = 2

numberOfVectors = 4

points = np.random.randint(5, size=(numberOfVectors, numberOfDimensions))

reshapedPoints = points.reshape(numberOfVectors, 1, numberOfDimensions)

distances = np.sqrt(np.sum((reshapedPoints - points) ** 2, axis=-1))

print(distances)

# one-liner

distances = np.sqrt(
    np.sum(
        (points.reshape(numberOfVectors, 1, numberOfDimensions) - points) ** 2, axis=-1
    )
)

print(distances)
