class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_fullname(self):
        return (f"{self.name} {self.surname}")

    def get_initials(self):
        return f"{self.name[0]}.{self.surname[0]}."


class Employee(Person):
    def __init__(self, name, surname, salary):
        super().__init__(name, surname)
        self.salary = salary

    # Геттер и сеттер зарплаты
    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary

    # Геттер и сеттер имени
    def get_name(self):
        return self.name

    def set_name(self, new_name):
        self.name = new_name

    # Геттер и сеттер фамилии
    def get_surname(self):
        return self.surname

    def set_surname(self, new_surname):
        self.surname = new_surname


employee = Employee("Larin", "Larinov", 50000)# Изначальные данные
print(employee.get_fullname())  # Larin Larinov
print(employee.get_initials())  # L. L.


# Замена

print(employee.get_salary(),end=" => ")  # 50000
employee.set_salary(60000)
print(employee.get_salary())  # 60000

print(employee.get_name(),end=" => ")  # Larin
employee.set_name("Gosha")
print(employee.get_name())  # Gosha


print(employee.get_surname(),end=" => ")  # Larinov
employee.set_surname("Valinov")
print(employee.get_surname())  # Valinov