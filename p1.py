class Employee:
    def __init__(self, emp_id, name, salary):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary  

    def display_details(self):
        print(f"Employee ID: {self.emp_id}")
        print(f"Name       : {self.name}")
        print(f"Monthly Sal: ${self.salary:,.2f}")


class Manager(Employee):
    def __init__(self, emp_id, name, salary, department):
        super().__init__(emp_id, name, salary)
        self.department = department

    def calculate_annual_salary(self):
        return self.salary * 12

    def display_details(self):
        super().display_details()
        print(f"Department : {self.department}")
        print(f"Annual Sal : ${self.calculate_annual_salary():,.2f}")

if __name__ == "__main__":
    print("--- General Employee Details ---")
    emp = Employee(101, "Alice Smith", 4500)
    emp.display_details()
    
    print("\n--- Manager Details & Annual Salary ---")
    mgr = Manager(201, "Bob Jones", 7500, "Engineering")
    mgr.display_details()
