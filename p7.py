import numpy as np

matrix_A = np.array([[1, 2], [3, 4], [5, 6]])
matrix_B = np.array([[7, 8, 9], [10, 11, 12]])

matrix_product = np.dot(matrix_A, matrix_B)

print("Matrix A (3x2):\n", matrix_A)
print("\nMatrix B (2x3):\n", matrix_B)
print("\nResulting Product Matrix (3x3):\n", matrix_product)
