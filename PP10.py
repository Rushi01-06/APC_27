import pandas as pd

price_dict = {"Laptop": 55000, "Mouse": 800, "Keyboard": 1500, "Monitor": 12000, "Cable": 250}
s = pd.Series(price_dict)

print("All products and prices:\n", s)

s_increased = s * 1.10
print("\nPrices increased by 10%:\n", s_increased)
print("\nMost expensive product:", s.idxmax(), "-", s.max())
print("\nProducts costing more than ₹1,000:\n", s[s > 1000])
