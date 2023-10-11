class Employee:

    name = None
    salary = None

    def showName(self):
        return f'name: {self.name}'

    def showSalary(self):
        return f'salary: {self.salary}'

emp = Employee()

emp.name = 'Аксинья'
emp.salary = 23510

print(emp.showName())