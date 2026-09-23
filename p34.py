from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Car(Vehicle):
    def start(self):
        return "Car engine started with ignition key. Ready to drive."

    def stop(self):
        return "Car engine stopped and parked."

class Bike(Vehicle):
    def start(self):
        return "Bike kick-started. Engine is running."

    def stop(self):
        return "Bike engine turned off."

class Bus(Vehicle):
    def start(self):
        return "Bus engine started with heavy ignition. Air brakes released."

    def stop(self):
        return "Bus stopped at the terminal and engine shut down."

if __name__ == "__main__":
    vehicles = [Car(), Bike(), Bus()]

    for vehicle in vehicles:
        print(vehicle.start())
        print(vehicle.stop())
        print()
