class Student:

    name = None
    surname = None

    def FI(self):
        print(self.name[0].upper(), end='.')
        print(self.surname[0].upper(), end='.')

std = Student()

std.name = 'аксинья'
std.surname = 'Сакичева'

std.FI()