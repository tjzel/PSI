import numpy as np

integers = np.random.randint(5,16,100)

print(np.bincount(integers).argmax())
