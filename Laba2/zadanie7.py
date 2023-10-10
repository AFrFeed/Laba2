class User:
    name = None
    salary = None

    def return_name(self):
        print(self.name)

    def return_salary(self):
        print(self.salary)


user = User()

user.name = 'Gena'
user.salary = 1000000

user.return_name()
user.return_salary()