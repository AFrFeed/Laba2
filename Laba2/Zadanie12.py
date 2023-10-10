class User:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def return_name(self):
        return self.name

    def return_salary(self):
        return self.salary

    def return_percent_salary(self):
        return self.salary * 0.1 + self.salary


user = User('Gosling', 10000)

print(user.return_name())
print(user.return_salary())
print(user.return_percent_salary())