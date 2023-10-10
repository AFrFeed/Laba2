class User:
    __name = None
    __salary = None
    __age = None

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    def set_age(self, age):
        self.__age = age


user = User()

user.set_name('Rain')
user.set_salary('100000')
user.set_age('43')

print(user.get_name())
print(user.get_salary())
print(user.get_age())