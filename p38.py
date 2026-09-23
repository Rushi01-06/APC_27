from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass

class Bus(Transport):
    def calculate_fare(self, distance):
        rate_per_km = 2.0
        return distance * rate_per_km

class Train(Transport):
    def calculate_fare(self, distance):
        rate_per_km = 1.5
        return distance * rate_per_km

class Taxi(Transport):
    def calculate_fare(self, distance):
        base_fare = 15.0
        rate_per_km = 5.0
        return base_fare + (distance * rate_per_km)

class Flight(Transport):
    def calculate_fare(self, distance):
        base_fare = 100.0
        rate_per_km = 8.0
        return base_fare + (distance * rate_per_km)

if __name__ == "__main__":
    distance = 150.0  # distance in kilometers
    
    transport_modes = [
        Bus(),
        Train(),
        Taxi(),
        Flight()
    ]

    for mode in transport_modes:
        fare = mode.calculate_fare(distance)
        print(f"Fare for {type(mode).__name__} over {distance} km: ${fare:.2f}")
