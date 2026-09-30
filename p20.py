import numpy as np

arr_3d = np.arange(1, 25).reshape(2, 3, 4)

print("First element:", arr_3d[0, 0, 0])
print("Last element:", arr_3d[-1, -1, -1])
print("Element at index [0,1,2]:", arr_3d[0, 1, 2])
print("Element at index [1,2,3]:", arr_3d[1, 2, 3])
