class Employee:
    """Attributes: Name, EmployeeID, Basic_Salary"""

    def __int__(self, name, emp_id, bas_sal):
        self.name = name
        self.emp_id = emp_id
        self.bas_sal = bas_sal

    def print(self):
        print("Employee Name: ", self.name)
        print("Employee ID: ", self.emp_id)
        print("Employee's Basic Salary: ", self.bas_sal)


class Manager(Employee):
    def __init__(self, name, emp_id, bas_sal):
        super().__int__(name, emp_id, bas_sal)
        self.total_sales = float(input("Enter The Total Sales In Units: "))
        self.bonus = 0.0
        self.salary = 0.0

    def compute_bonus(self):
        if self.total_sales > 10000:
            self.bonus = (0.05 * self.bas_sal)
        else:
            self.bonus = (0.2 * self.bas_sal)

    def sal(self):
        self.salary = self.bas_sal + 0.12 * self.bas_sal + self.bonus

    def print_details(self):
        print("Total Sale In Units: ", self.total_sales)
        print("Bonus Achieved: ", self.bonus)
        print("Total Salary Inclusive Of Basic Salary, DA @ 12% And Bonus Achieved: ", self.salary)


employee_name = input("Enter The Employee Name: ")
employee_id = input("Enter The Employee ID: ")
basic_salary = float(input("Enter The Basic Salary: "))
m = Manager(employee_name, employee_id, basic_salary)
m.print()
m.compute_bonus()
m.sal()
m.print_details()