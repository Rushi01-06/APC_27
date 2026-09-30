import pandas as pd

salary_dict = {"Ananya": 54000, "Diya": 48000, "Isha": 62000, "Kavya": 42000, "Meera": 71000}
s = pd.Series(salary_dict)

print("Series:\n", s)
print("\nHighest Salary:", s.max())
print("Lowest Salary:", s.min())
print("Average Salary:", s.mean())
print("\nEmployees earning more than ₹50,000:\n", s[s > 50000])
