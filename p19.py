import numpy as np

arr_3d = np.arange(1, 25).reshape(2, 3, 4)

print("3D Array:\n", arr_3d)
print("\nNumber of dimensions:", arr_3d.ndim)
print("Shape:", arr_3d.shape)
print("Size:", arr_3d.size)
