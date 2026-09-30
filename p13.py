import numpy as np

arr = np.array([42, 7, 19, 88, 3, 54, 31])
print("Original Array:", arr)

asc_arr = np.sort(arr)
desc_arr = np.sort(arr)[::-1]

print("Ascending order:", asc_arr)
print("Descending order:", desc_arr)
