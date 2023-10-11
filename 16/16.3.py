class Employee:
    __name = None
    __age = None
    __salary = None

    def __init__(self, name: str, age: int, salary: str):
        self.__name = name
        self.__age = age
        self.__salary = salary

    def getName(self):
        return self.__name

    def getAge(self):
        return self.__age

    def getSalary(self):
        return self.__salary

emp = Employee('Аксинья', 18, 23510)
