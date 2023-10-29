class Validator:

    def __init__(self, str: str):
        self.string = str
        self.dominal = {
            'com': 1,
            'ru':2,
            'gov':3
        }

    def isEmail(self):
        if (self.string.find('@') != -1):
            print('Строка это корректный email')
        else:
            print('Строка это некорректный email')

    def isDomain(self):
        if ( self.dominal[self.string[self.string.find('.')+1:]] != 0):
            print('Домен корректный')
        else:
            print('Домен не корректный')


validator = Validator('skjldfgh:gmail.com')

validator.isDomain()