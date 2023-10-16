class User:
  def setName(self,name):
    self.name = name

  def greet(self):
      print("Hello, I'm a John!")

  def getName(self):
    return self.name
class Employee(User):
  def work(self):
    print("I'm working!")

employee = Employee()
employee.greet()
employee.setName('John')
name = employee.getName()
print(name)