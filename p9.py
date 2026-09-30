import numpy as np

matrix = np.arange(1, 17).reshape(4, 4)

print("Matrix (4x4):\n", matrix)
print("\nFirst Row:", matrix[0, :])
print("Last Column:", matrix[:, -1])
print("Diagonal Elements:", np.diag(matrix))
print("Second and Third Rows:\n", matrix[1:3, :])
