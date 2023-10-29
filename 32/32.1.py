class User:
    def setAge(self, age):
        if (age >= 0):
            self.age = age
        else:
            raise Exception('need age more 0')


class Employee(User):
    pass


emp = Employee()
emp.setAge(18)

print(emp.age)