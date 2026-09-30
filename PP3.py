import pandas as pd

data = {
    "Product ID":,
    "Product Name": ["Laptop", "Mouse", "Keyboard", "Monitor", "Headphones"],
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
    "Price":,
    "Quantity": [5, 50, 30, 10, 25]
}

df = pd.DataFrame(data)
df["Total Amount"] = df["Price"] * df["Quantity"]

print("DataFrame:\n", df)
print("\nProduct with highest total sales:\n", df.loc[df["Total Amount"].idxmax()])
