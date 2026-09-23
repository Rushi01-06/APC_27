class Distance:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches
        self._normalize()

    def _normalize(self):
        if self.inches >= 12:
            self.feet += self.inches // 12
            self.inches %= 12

    def __add__(self, other):
        total_feet = self.feet + other.feet
        total_inches = self.inches + other.inches
        return Distance(total_feet, total_inches)

    def __str__(self):
        return f"{self.feet} feet, {self.inches} inches"

if __name__ == "__main__":
    d1 = Distance(5, 8)
    d2 = Distance(3, 7)
    
    d3 = d1 + d2
    print(f"Distance 1: {d1}")
    print(f"Distance 2: {d2}")
    print(f"Sum (Normalized): {d3}")
