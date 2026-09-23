class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __gt__(self, other):
        return self.price > other.price

    def __str__(self):
        return f"{self.name} (${self.price})"

if __name__ == "__main__":
    p1 = Product("Laptop", 1200)
    p2 = Product("Phone", 800)
    p3 = Product("Tablet", 800)

    print(p1)
    print(p2)
    print(p3)

    print(f"Is {p1.name} more expensive than {p2.name}? {p1 > p2}")
    print(f"Is {p2.name} equal in price to {p3.name}? {p2 == p3}")
