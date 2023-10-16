class Person:
    def __private_method(self):
        print("Приватный метод")

    def public_method(self):
        print("Публичный метод")
        self.__private_method()

class Employee(Person):
    def public_method(self):
        print("Публичный метод")
        self._Person__private_method()


employee = Employee()
employee.public_method()