import numpy as np

np.random.seed(42)
arr_rand = np.random.randint(1, 101, size=(2, 3, 4))
print("Original Random Array:\n", arr_rand)

arr_rand[arr_rand > 50] = 0
print("\nModified Array:\n", arr_rand)
