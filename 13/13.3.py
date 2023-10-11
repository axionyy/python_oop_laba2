class Employee:
    def __init__(self, name: str, age: int, salary: int):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def output(self):
        print(f"name: {emp.__name}"
              f"\nage: {emp.__age}"
              f"\nsalary: {emp.__salary}")
        
emp = Employee('Аксинья', 18, 23510)

emp.output()