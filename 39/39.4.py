class User:
    def setName(self, name):
        self.__name = name


class Employee(User):
    def setSalary(self, surname):
        self.__surname = surname


class Programmer(Employee):
    def setAge(self, age):
        self.__age = age


class Designer(Employee):
    def setStage(self, salary):
        self.__salary = salary
