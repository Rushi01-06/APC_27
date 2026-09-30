import numpy as np

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

h_concat = np.hstack((arr1, arr2))
v_concat = np.vstack((arr1, arr2))

print("Horizontal Concatenation:\n", h_concat)
print("\nVertical Concatenation:\n", v_concat)
