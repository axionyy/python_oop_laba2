class User:
    name = None
    salary = None

    def show(self,name, salary):
        return name + ' ' + salary

emp = User()

#emp.name = 'Аксинья'
#emp.salary = 23510

print(emp.show('Аксинья','23510'))