import pandas as pd

df = pd.read_csv("patients.csv")

print("Patients above 60 years:\n", df[df["Age"] > 60])
print("\nAverage Medical Expense:", df["Medical_Expense"].mean())
print("\nPatient with highest medical expense:\n", df.loc[df["Medical_Expense"].idxmax()])
print("\nPatient count per disease:\n", df["Disease"].value_counts())
print("\nPatients whose medical expense exceeds ₹50,000:\n", df[df["Medical_Expense"] > 50000])
