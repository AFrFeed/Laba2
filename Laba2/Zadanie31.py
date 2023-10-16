class Employee:
    def __init__(self, age):
        self._age = age

    def get_age(self):
        return self._age

    def set_age(self, age):
        if 18 <= age <= 65:
            self._age = age
        else:
            print("Возраст должен быть от 18 до 65 лет")


employee = Employee(30)
print(employee.get_age())  # 30

employee.set_age(25)
print(employee.get_age())  # 25

employee.set_age(70)  # ValueError: Возраст должен быть от 18 до 65 лет
