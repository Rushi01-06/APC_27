import numpy as np

arr_3d = np.arange(1, 24).reshape(2, 3, 4)

print("Sum of all elements:", np.sum(arr_3d))
print("Sum of each layer:\n", np.sum(arr_3d, axis=(1, 2)))
print("Sum along rows:\n", np.sum(arr_3d, axis=2))
print("Sum along columns:\n", np.sum(arr_3d, axis=1))
