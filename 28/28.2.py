class User:
    name = None
    surname = None


class Employee:
    pass


class Employee(User):
    pass


user = Employee()
user.name = "Millie Bobby"
user.surname = "Brown"
print("Имя:", user.name, "\nФамилия:", user.surname)
