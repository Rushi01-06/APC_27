import numpy as np

numbers = np.arange(1, 21)

even_mask = (numbers % 2 == 0)
odd_mask = (numbers % 2 != 0)

even_numbers = numbers[even_mask]
odd_numbers = numbers[odd_mask]

print("Original Array:", numbers)
print("Even Numbers:  ", even_numbers)
print("Odd Numbers:   ", odd_numbers)
