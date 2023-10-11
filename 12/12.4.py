class Employee:
    def __init__(self, name: str, age: int, salary: int):
        self.name = name
        self.age = age
        self.salary = salary

    def outputName(self):
        print(self.name)

    def outputSalary(self):
        print(self.salary)

    def salary10p(self):
        print(f'salary1: {self.salary}'
              f'\nsalary2: {self.salary * 1.1}')

emp = Employee('Аксинья', 18, 23510)