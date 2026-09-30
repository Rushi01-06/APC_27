import numpy as np

np.random.seed(42)
arr = np.random.randint(1, 101, size=(3, 4, 5))
flat = arr.flatten()
avg = np.mean(flat)

print("Elements > 50:\n", flat[flat > 50])
print("\nEven elements:\n", flat[flat % 2 == 0])
print("\nElements < average (Average = {}):\n".format(round(avg, 2)), flat[flat < avg])
