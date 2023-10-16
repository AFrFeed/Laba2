class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

employees = [
Employee("John", 30000),
Employee("Libert", 20000),
Employee("Skybi", 10000)
]

for employee in employees:
    print(employee.name, employee.salary)