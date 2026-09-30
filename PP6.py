import pandas as pd

data = {
    "Student_ID":,
    "Name": ["Arjun", "Neha", "Rohan", "Sneha", "Yash"],
    "Department": ["CSE", "ECE", "CSE", "ME", "ECE"],
    "Total_Classes":,
    "Classes_Attended": [32, 26, 45, 30, 42]
}

df = pd.DataFrame(data)
df["Attendance Percentage"] = (df["Classes_Attended"] / df["Total_Classes"]) * 100

print("Students with attendance below 75%:\n", df[df["Attendance Percentage"] < 75])
