import pandas as pd

marks_dict = {"Aarav": 82, "Vivaan": 68, "Aditya": 91, "Sai": 74, "Reyansh": 85}
s = pd.Series(marks_dict)

print("Series:\n", s)
print("\nMarks of Aditya:", s["Aditya"])
print("Maximum Marks:", s.max())
print("Minimum Marks:", s.min())
print("Average Marks:", s.mean())
print("\nStudents scoring more than 75:\n", s[s > 75])
