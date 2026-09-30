import numpy as np

array_1d = np.arange(1, 13)

matrix_2x6 = array_1d.reshape(2, 6)
matrix_3x4 = array_1d.reshape(3, 4)
matrix_4x3 = array_1d.reshape(4, 3)

print("Original 1D Array:\n", array_1d)
print("\nReshaped 2x6 Matrix:\n", matrix_2x6)
print("\nReshaped 3x4 Matrix:\n", matrix_3x4)
print("\nReshaped 4x3 Matrix:\n", matrix_4x3)
