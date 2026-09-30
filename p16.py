import numpy as np

marks = np.array([78, 85, 92, 64, 89, 73, 95, 81, 68, 90])

print("Highest marks:", np.max(marks))
print("Lowest marks:", np.min(marks))
print("Average marks:", np.mean(marks))
print("Median:", np.median(marks))
print("Standard deviation:", round(np.std(marks), 2))
