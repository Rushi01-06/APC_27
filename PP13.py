import pandas as pd

df = pd.read_csv("students.csv")

print("First 5 records:\n", df.head(5))
print("\nLast 5 records:\n", df.tail(5))

df["Total"] = df["Python"] + df["DBMS"] + df["Maths"]
df["Average"] = df["Total"] / 3

print("\nData with Totals and Averages:\n", df[["Student_ID", "Name", "Total", "Average"]])
print("\nStudents with average > 75:\n", df[df["Average"] > 75])
print("\nStudent with highest average:\n", df.loc[df["Average"].idxmax()])

print("\nAverage marks per subject:\n", df[["Python", "DBMS", "Maths"]].mean())
