class User:
    def __init__(self, name):
        self.name = name

class Employee(User):
    def __init__(self, name, age, salary):
        super().__init__(name)
        self.age = age
        self.salary = salary

    def get_age(self):
        return self.age

    def get_salary(self):
        return self.salary

employee = Employee("Djon Biden", 30000, 5000000)
print(employee.get_age())
print(employee.get_salary())
