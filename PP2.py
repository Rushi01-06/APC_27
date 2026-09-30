import pandas as pd

data = {
    "Employee ID":,
    "Employee Name": ["Ananya", "Diya", "Isha", "Kavya", "Meera"],
    "Department": ["IT", "HR", "CSE", "IT", "CSE"],
    "Salary":,
    "Experience": [4, 2, 6, 3, 8]
}

df = pd.DataFrame(data)

print("Employees with salary > ₹50,000:\n", df[df["Salary"] > 50000])
print("\nAverage Salary:", df["Salary"].mean())
print("Highest Salary:", df["Salary"].max())
print("\nEmployee with highest experience:\n", df.loc[df["Experience"].idxmax()])
