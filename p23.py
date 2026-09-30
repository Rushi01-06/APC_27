import numpy as np

np.random.seed(42)
arr = np.random.randint(1, 100, size=(3, 4, 5))

print("Mean:", round(np.mean(arr), 2))
print("Median:", np.median(arr))
print("Standard Deviation:", round(np.std(arr), 2))
print("Variance:", round(np.var(arr), 2))
print("Minimum:", np.min(arr))
print("Maximum:", np.max(arr))
