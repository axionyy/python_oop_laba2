class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class EmployeesCollection:
    def __init__(self):
        self.employees = []


class EmployeesCollection:
    def __init__(self):
        self.employees = []

    def new_employee(self, name, salary):
        employee_new = Employee(name, salary)
        self.employees.append(employee_new)

    def list_employees(self):
        for employee in self.employees:
            print(f"Имя: {employee.name}, Зарплата: {employee.salary}")
