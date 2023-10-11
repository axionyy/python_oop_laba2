class Employee:
    __name = None
    __age = None
    __salary = None

    def __init__(self, name:str,age:int, salary:str):
        self.__name = name
        self.__age = age
        self.__salary = salary