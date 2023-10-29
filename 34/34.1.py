class User:
    def __get(self):
        return 'ты кто?'


class Employee(User):
    pass


emp = Employee()
emp.__get()
