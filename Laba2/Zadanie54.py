class Rectangle:
    def __init__(self):
        self.width = None
        self.height = None

    def getSquare(self):
        return self.width * self.height

    def getPerimeter(self):
        return (self.width + self.height) * 2

    def getRatio(self):
        return self.getSquare() / self.getPerimeter()

rectangle = Rectangle()

rectangle.width = 6
rectangle.height = 12

print(rectangle.getSquare())
print(rectangle.getPerimeter())
print(rectangle.getRatio())