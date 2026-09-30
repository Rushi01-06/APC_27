import pandas as pd

data = {
    "Product_ID":,
    "Product_Name": ["Desk", "Chair", "Lamp", "Shelf", "Rug"],
    "Category": ["Furniture", "Furniture", "Decor", "Furniture", "Decor"],
    "Price":,
    "Quantity": [2, 4, 10, 1, 5]
}

df = pd.DataFrame(data)
df["Total_Sales"] = df["Price"] * df["Quantity"]

print("Products with sales greater than ₹10,000:\n", df[df["Total_Sales"] > 10000])
print("\nProduct with maximum sales:\n", df.loc[df["Total_Sales"].idxmax()])
print("\nAverage sales:", df["Total_Sales"].mean())
