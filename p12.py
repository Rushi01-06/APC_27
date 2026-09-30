import numpy as np

arr = np.array([15, 62, 45, 98, 23, 50, 71, 12, 88, 34])
print("Original Array:", arr)

arr[arr > 50] = 0
print("Modified Array:", arr)
