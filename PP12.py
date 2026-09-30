import pandas as pd

att_dict = {"Arjun": 85.0, "Neha": 68.5, "Rohan": 94.2, "Sneha": 72.0, "Yash": 91.5}
s = pd.Series(att_dict)

print("Average Attendance:", s.mean())
print("\nStudents with attendance below 75%:\n", s[s < 75])
print("\nStudents with attendance above 90%:\n", s[s > 90])
print("\nHighest Attendance:", s.max())
