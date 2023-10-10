# Это код выводи ошибку поскольку ет оператора instanceof. и выведет ошибку
# Для того чтоб код исправно работал нужно переписать код с использованием instanceof.
#    class Student:
#        pass
#
#
#    class Employee:
#        pass
#
#
#    employee = Employee
#    print(employee instanceof; Employee)
#    print(employee instanceof; Student)


# При использовании такого метода синтаксической ошибки не произойдет и код запустится.
class Student:
    pass


class Employee:
    pass


employee = Employee()
print(isinstance(employee, Employee))
print(isinstance(employee, Student))

class Student:
  def __init__(self, name):
    self.name = name

class Employee:
  def __init__(self, name):
    self.name = name

users = [
   Student('Rain Gosling'),
   Employee('Maik Vazovski'),
   Student('John Libert'),
   Employee('Piter Pedegri'),
   Student('Romen Fychers'),
   Employee('Raizen Kaybzer'),
   Student('Byren Gavrelin'),
]

for user in users:
  if isinstance(user, Employee):
    print(user.name)