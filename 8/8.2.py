class Student:
    name = None
    surname = None


    def upperLetter(self, str):
        for i in range(len(str)):
            if i != 0:
                print(str[i], end='')
            else:
                print(str[i].upper(), end='')

std = Student()

std.name = 'аксинья'
std.surname = 'Сакичева'

std.upperLetter(std.name)