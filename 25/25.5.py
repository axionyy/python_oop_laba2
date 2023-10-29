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

class EmployeesCollection:
    def __init__(self):
        self.employees = []

    def new_employee(self, name, salary):
        employee_new = Employee(name, salary)
        self.employees.append(employee_new)

    def list_employees(self):
        for employee in self.employees:
            print(f"Имя: {employee.name}, Зарплата: {employee.salary}")

    def total_salary(self):
        total = sum(employee.salary for employee in self.employees)
        return total

class EmployeesCollection:
    def __init__(self):
        self.employees = []

    def new_employee(self, name, salary):
        employee_new = Employee(name, salary)
        self.employees.append(employee_new)

    def list_employees(self):
        for employee in self.employees:
            print(f"Имя: {employee.name}, Зарплата: {employee.salary}")

    def total_salary(self):
        total = sum(employee.salary for employee in self.employees)
        return total

class EmployeesCollection:
    def __init__(self):
        self.employees = []

    def new_employee(self, name, salary):
        employee_new = Employee(name, salary)
        self.employees.append(employee_new)

    def list_employees(self):
        for employee in self.employees:
            print(f"Имя: {employee.name}, Зарплата: {employee.salary}")

    def total_salary(self):
        total = sum(employee.salary for employee in self.employees)
        return total

    def average_salary(self):
        total = self.total_salary()
        count = len(self.employees)
        if count == 0:
            return 0
        average = total / count
        return average


employee_collection = EmployeesCollection()

employee_collection.new_employee("Алевтина", 70000)
employee_collection.new_employee("Мария", 40000)
employee_collection.new_employee("Ольга", 120000)

employee_collection.list_employees()

total_salary = employee_collection.total_salary()
print(f"Суммарная зарплата: {total_salary}")

average_salary = employee_collection.average_salary()
print(f"Средняя зарплата: {average_salary}")
