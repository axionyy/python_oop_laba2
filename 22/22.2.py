class Validator:

    def __init__(self, str: str):
        self.string = str

    def isEmail(self):
        if (self.string.find('@') != -1):
            print('Строка это корректный email')
        else:
            print('Строка это некорректный email')


validator = Validator('skjldfgh:gmail.com')

validator.isEmail()