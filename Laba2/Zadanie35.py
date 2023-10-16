class User:
    __name = None
    __surname = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setSurn(self,surname): #Добавил self код выдовал ошибку  takes 1 positional argument but 2 were given
        self.__surname = surname

    def getSurn(self):
        return self.__surname
class Employee(User):
    def getFull(self):
        return self.getName() + ' ' + self.getSurn()

employee = Employee()
employee.setName("Djoni")
employee.setSurn("Rysbert")

print(employee.getName())
print(employee.getSurn())
print(employee.getFull())