class User:
    __name = None
    __salary = None

    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary

    def getSalary(self):
        return self.__addSign(self.__salary)

    def __addSign(self, num):
        return num + '$'


user = User('Gosling', '100000')
print(user.getSalary())