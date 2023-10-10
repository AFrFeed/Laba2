class Car:
    def __init__(self):
        self.model = "BMW"
        self.year = 2020
        self.brand = "X5"
        self.color = "black"

    def print_model(self):
        print("Model:", self.model)

    def print_year(self):
        print("Year:", self.year)

    def print_brand(self):
        print("Brand:", self.brand)

    def print_color(self):
        print("Color:", self.color)


car = Car()
car.print_model()
car.print_year()
car.print_brand()
car.print_color()