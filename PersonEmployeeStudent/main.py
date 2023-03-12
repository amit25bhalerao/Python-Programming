class Person:
    """Attributes: Name, Address"""

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def calculate(self):
        pass

    def print(self):
        pass


class Employee(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.salary = float(input("Enter The Salary Of Employee: "))
        self.increment = float(input("Enter The Increment To Be Given: "))
        self.new_salary = 0.0

    def calculate(self):
        self.new_salary = self.salary + self.increment

    def print(self):
        print("Name Of Employee: ", self.name)
        print("Address Of Employee: ", self.address)
        print("Old Salary: ", self.salary)
        print("Increment: ", self.increment)
        print("New Salary: ", self.new_salary)


class Student(Person):
    def __init__(self, name, address):
        super().__init__(name, address)
        self.m1 = float(input("Enter The Marks Obtained In Subject 1: "))
        self.m2 = float(input("Enter The Marks Obtained In Subject 2: "))
        self.m3 = float(input("Enter The Marks Obtained In Subject 3: "))

    def calculate(self):
        if self.m1 >= self.m3 and self.m2 >= self.m3:
            print("Two Best Marks Obtained Are {} And {}".format(self.m1, self.m2))
        elif self.m1 >= self.m2 and self.m3 >= self.m2:
            print("Two Best Marks Obtained Are {} And {}".format(self.m1, self.m3))
        else:
            print("Two Best Marks Obtained Are {} And {}".format(self.m2, self.m3))

    def print(self):
        print("Student Name: ", self.name)
        print("Address Of Student: ", self.address)


employee_name = input("Enter The Name Of The Employee: ")
employee_address = input("Enter The Address Of The Employee: ")
e = Employee(employee_name, employee_address)
e.calculate()
e.print()

student_name = input("Enter The Name Of The Student: ")
student_address = input("Enter The Address Of The Student: ")
s = Student(student_name, student_address)
s.print()
s.calculate()