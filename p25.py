import numpy as np

arr_3d = np.arange(1, 28).reshape(3, 3, 3)
flat = arr_3d.flatten()

print("Sum:", np.sum(flat))
print("Average:", np.mean(flat))
print("Maximum:", np.max(flat))
print("Minimum:", np.min(flat))
