import numpy as np

matrix = np.arange(1, 17).reshape(4, 4)
row_sums = np.sum(matrix, axis=1)
col_sums = np.sum(matrix, axis=0)

print("Matrix:\n", matrix)
print("\nSum of each row:", row_sums)
print("Sum of each column:", col_sums)
