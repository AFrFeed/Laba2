class User:
    __name = None
    __salary = None
    __age = None

    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_age(self):
        return self.__age


user = User('Gosling', 100000, 43)
print(user.get_name())
print(user.get_salary())
print(user.get_age())