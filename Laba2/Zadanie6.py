class User:
    def t_pass(self, name, salary):
        return name + ' - ' + salary


user = User()

print(user.t_pass('Fantomka', '12000'))