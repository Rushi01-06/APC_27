import numpy as np

matrix = np.arange(1, 13).reshape(3, 4)
transpose = matrix.T

print("Original Matrix (3x4):\n", matrix)
print("\nTransposed Matrix (4x3):\n", transpose)
