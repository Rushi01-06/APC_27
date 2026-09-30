import pandas as pd

age_dict = {501: 65, 502: 45, 503: 72, 504: 38, 505: 61}
s = pd.Series(age_dict)

print("Average Age:", s.mean())
print("Oldest Patient Age:", s.max())
print("Youngest Patient Age:", s.min())
print("\nPatients above 60 years:\n", s[s > 60])
