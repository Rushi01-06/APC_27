import pandas as pd

df = pd.read_csv("employees.csv")

print("Employees from CSE department:\n", df[df["Department"] == "CSE"])
print("\nAverage Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("Lowest Salary:", df["Salary"].min())
print("\nEmployees with salary > ₹50,000:\n", df[df["Salary"] > 50000])
print("\nDepartment-wise average salary:\n", df.groupby("Department")["Salary"].mean())
