class User:
    __name = None
    __salary = None
    __age = None

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def return_info(self):
        print(self.__name, self.__salary, self.__age)


user = User('Gosling', 100000, 43)

user.return_info()