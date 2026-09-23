from abc import ABC, abstractmethod

class Appointment(ABC):
    def __init__(self, patient_name, date):
        self.patient_name = patient_name
        self.date = date

    @abstractmethod
    def book_appointment(self):
        pass

    @abstractmethod
    def calculate_fee(self):
        pass

class GeneralAppointment(Appointment):
    def __init__(self, patient_name, date, base_fee=50.0):
        super().__init__(patient_name, date)
        self.base_fee = base_fee

    def book_appointment(self):
        return f"General appointment booked for {self.patient_name} on {self.date}."

    def calculate_fee(self):
        return self.base_fee

class SpecialistAppointment(Appointment):
    def __init__(self, patient_name, date, specialist_fee=150.0):
        super().__init__(patient_name, date)
        self.specialist_fee = specialist_fee

    def book_appointment(self):
        return f"Specialist consultation booked for {self.patient_name} on {self.date}."

    def calculate_fee(self):
        return self.specialist_fee + 30.0

class EmergencyAppointment(Appointment):
    def __init__(self, patient_name, date, emergency_fee=300.0):
        super().__init__(patient_name, date)
        self.emergency_fee = emergency_fee

    def book_appointment(self):
        return f"Emergency priority appointment registered immediately for {self.patient_name} on {self.date}."

    def calculate_fee(self):
        return self.emergency_fee + 100.0

if __name__ == "__main__":
    appointments = [
        GeneralAppointment("Alice", "2026-09-25"),
        SpecialistAppointment("Bob", "2026-09-26"),
        EmergencyAppointment("Charlie", "2026-09-23")
    ]

    for appt in appointments:
        print(appt.book_appointment())
        print(f"Total Fee: ${appt.calculate_fee():.2f}")
        print()
