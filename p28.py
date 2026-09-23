class Student:
    def __init__(self, name, total_marks):
        self.name = name
        self.total_marks = total_marks

    def __gt__(self, other):
        return self.total_marks > other.total_marks

    def __lt__(self, other):
        return self.total_marks < other.total_marks

    def __str__(self):
        return f"{self.name} ({self.total_marks} marks)"

if __name__ == "__main__":
    student1 = Student("Alice", 88)
    student2 = Student("Bob", 94)

    print(student1)
    print(student2)

    print(f"Is {student1.name} > {student2.name}? {student1 > student2}")
    print(f"Is {student1.name} < {student2.name}? {student1 < student2}")
