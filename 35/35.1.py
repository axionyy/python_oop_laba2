class User:
    __name = None
    __surname = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSurn(self, surname):
        self.__surname = surname

    def getSurn(self):
        return self.__surname


class Employee(User):
    pass


emp = Employee()

emp.setName('Ольга')
emp.setSurn('Парфенюк')

print(emp.getName(), end=" ")
print(emp.getSurn())
