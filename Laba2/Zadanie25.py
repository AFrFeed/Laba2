class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


class EmployeesCollection:
    def __init__(self):
        self.employees = []

    def addEmployee(self, name, salary):
        employee = Employee(name, salary)
        self.employees.append(employee)

    def showEmployees(self):
        for employee in self.employees:
            print(employee.name,employee.salary)

    def total_salary(self):
        total_salary = 0
        for employee in self.employees:
            total_salary += employee.salary
        return total_salary

    def average_salary(self):
        if len(self.employees) == 0:
            return 0
        total_salary = self.total_salary()
        average_salary = total_salary / len(self.employees)
        return average_salary


# Пример использования
# Создание экземпляра класса EmployeesCollection
ec = EmployeesCollection()

# Добавление работников
ec.addEmployee("John", 2000)
ec.addEmployee("Mary", 2500)

# Вывод всех работников
ec.showEmployees()

# Расчет суммарной зарплаты
total_salary = ec.total_salary()
print("Total salary:", total_salary)

# Расчет средней зарплаты
average_salary = ec.average_salary()
print("Average salary:", average_salary)

