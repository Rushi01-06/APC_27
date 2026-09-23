from abc import ABC, abstractmethod

class Patient(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def treatment(self):
        pass

    @abstractmethod
    def calculate_bill(self):
        pass

class InPatient(Patient):
    def __init__(self, name, age, days_admitted, room_charge_per_day):
        super().__init__(name, age)
        self.days_admitted = days_admitted
        self.room_charge_per_day = room_charge_per_day

    def treatment(self):
        return f"{self.name} is admitted for continuous observation and specialist care."

    def calculate_bill(self):
        return (self.days_admitted * self.room_charge_per_day) + 500.0

class OutPatient(Patient):
    def __init__(self, name, age, consultation_fee):
        super().__init__(name, age)
        self.consultation_fee = consultation_fee

    def treatment(self):
        return f"{self.name} received a routine doctor consultation and prescription."

    def calculate_bill(self):
        return self.consultation_fee

class EmergencyPatient(Patient):
    def __init__(self, name, age, emergency_fee, procedural_cost):
        super().__init__(name, age)
        self.emergency_fee = emergency_fee
        self.procedural_cost = procedural_cost

    def treatment(self):
        return f"{self.name} underwent immediate trauma care and emergency intervention."

    def calculate_bill(self):
        return self.emergency_fee + self.procedural_cost + 1000.0

if __name__ == "__main__":
    patients = [
        InPatient("Alice", 45, 4, 250.0),
        OutPatient("Bob", 30, 80.0),
        EmergencyPatient("Charlie", 52, 600.0, 450.0)
    ]

    for patient in patients:
        print(f"Patient: {patient.name} ({type(patient).__name__})")
        print(patient.treatment())
        print(f"Total Bill: ${patient.calculate_bill():.2f}")
        print()
