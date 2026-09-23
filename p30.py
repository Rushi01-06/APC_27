class Person:
    def display_role(self):
        return "Role: Person"

class Student(Person):
    def display_role(self):
        return "Role: Student"

class Faculty(Person):
    def display_role(self):
        return "Role: Faculty"

class Administrator(Person):
    def display_role(self):
        return "Role: Administrator"

if __name__ == "__main__":
    people = [
        Student(),
        Faculty(),
        Administrator()
    ]

    for person in people:
        print(person.display_role())
