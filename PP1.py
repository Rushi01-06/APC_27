import pandas as pd

data = {
    "Student ID":,
    "Student Name": ["Aarav", "Vivaan", "Aditya", "Sai", "Reyansh"],
    "Python Marks":,
    "DBMS Marks":,
    "Mathematics Marks": [92, 60, 88, 75, 79]
}

df = pd.DataFrame(data)
df["Total Marks"] = df["Python Marks"] + df["DBMS Marks"] + df["Mathematics Marks"]
df["Average Marks"] = df["Total Marks"] / 3

print("DataFrame:\n", df)
print("\nStudents with Average > 75%:\n", df[df["Average Marks"] > 75])
