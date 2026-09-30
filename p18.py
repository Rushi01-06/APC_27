import numpy as np

marks = np.array([55, 78, 82, 45, 93, 67, 72, 88, 61, 59, 90, 74, 83, 49, 91, 66, 70, 85, 77, 63])
avg = np.mean(marks)
above_avg = marks[marks > avg]

print("Class Average:", avg)
print("Marks above average:", above_avg)
