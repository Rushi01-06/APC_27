import pandas as pd

data = {
    "Patient ID":,
    "Patient Name": ["Ramesh", "Suresh", "Kamla", "Vimla", "Jagdish"],
    "Age":,
    "Disease": ["Diabetes", "Flu", "Blood Pressure", "Malaria", "Diabetes"],
    "Medical Charges": [45000, 12000, 65000, 8000, 55000]
}

df = pd.DataFrame(data)

print("Patients above 60 years:\n", df[df["Age"] > 60])
print("\nAverage Medical Charge:", df["Medical Charges"].mean())
print("Maximum Medical Charge:", df["Medical Charges"].max())
print("\nPatients with charges > ₹50,000:\n", df[df["Medical Charges"] > 50000])
