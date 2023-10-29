class Employee:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getInfo(self):
        return self.__name, self.__salary

stuffs = [
    Employee('Аксинья', 23510),
    Employee('Евгения', 149302),
    Employee('Арина', 4520)
]

for i in stuffs:
    print(i.getInfo())
