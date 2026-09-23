from abc import ABC, abstractmethod

class FoodOrder(ABC):
    def __init__(self, items_cost):
        self.items_cost = items_cost

    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass

class RestaurantOrder(FoodOrder):
    def __init__(self, items_cost, service_tax_rate=0.05):
        super().__init__(items_cost)
        self.service_tax_rate = service_tax_rate

    def calculate_bill(self):
        tax = self.items_cost * self.service_tax_rate
        return self.items_cost + tax + self.delivery_charge()

    def delivery_charge(self):
        return 0.0

class HomeDeliveryOrder(FoodOrder):
    def __init__(self, items_cost, distance_km, base_fee=5.0):
        super().__init__(items_cost)
        self.distance_km = distance_km
        self.base_fee = base_fee

    def calculate_bill(self):
        return self.items_cost + self.delivery_charge()

    def delivery_charge(self):
        return self.base_fee + (self.distance_km * 1.5)

if __name__ == "__main__":
    restaurant_order = RestaurantOrder(45.00)
    delivery_order = HomeDeliveryOrder(45.00, 6.0)

    print(f"Restaurant Order Total: ${restaurant_order.calculate_bill():.2f} (Delivery: ${restaurant_order.delivery_charge():.2f})")
    print(f"Home Delivery Order Total: ${delivery_order.calculate_bill():.2f} (Delivery: ${delivery_order.delivery_charge():.2f})")
