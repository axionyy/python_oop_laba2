class Employee:
    pass

emp1 = Employee()
emp2 = Employee()

emp1.name = 'Аксинья'
emp1.salary = 23510

emp2.name = 'Евгения'
emp2.salary = 98712
print(f'total salary: {emp1.salary + emp2.salary}')