import math

class Point:
    def __init__(self, x=0.00, y=0.00):
        self.x = x
        self.y = y

    def printinfo(self):
        print(f"Position: {self.x}, {self.y};", end = "")

class Circle(Point):
    def __init__(self, x = 0.00, y = 0.00, radius=0):
        super().__init__(x, y)
        self.radius = radius

    def area(self):
        self.a = self.radius * self.radius * math.pi
        return self.a

    def printinfo(self):
        super().printinfo()
        print(f" Radius: {self.radius}; Area: {self.area()}")

circle1 = Circle(5, 5, 10)
circle2 = Circle(10, 10, 5)
circle3 = Circle(radius=10)
circle1.printinfo()
circle2.printinfo()
circle3.printinfo()
