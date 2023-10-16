class User:
    name = None
    position = None
    department = None

    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department

class Position:
    title = None

    def __init__(self, title):
        self.title = title

class Department:
    name = None

    def __init__(self, name):
        self.name = name

# Создание объектов Position и Department
position = Position('Менеджер')
department = Department('Отдел связи')
user = User('Ларенсо', position, department)

print("Имя:", user.name)
print("Должность:", user.position.title)
print("Отдел:", user.department.name)