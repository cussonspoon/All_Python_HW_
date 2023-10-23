#Question 3.2
import math
import turtle
class Circle:
    def __init__(self, x = 0, y = 0, radius = 0):
        self.x = x
        self.y = y
        self.radius = radius
    def getArea(self):
        Area = math.pi*self.radius*self.radius
        return Area
    def getPerimeter(self):
        P = 2*math.pi*self.radius
        return P
    def move(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        turtle.speed(10)
        turtle.penup()
        turtle.goto(self.x, self.y)
        turtle.right(90)
        turtle.forward(self.radius)
        turtle.left(90)
        turtle.pendown()
        turtle.circle(self.radius)
        turtle.penup()
        turtle.goto(self.x, self.y)

c = Circle(0, 0, 100)
print(c.getArea())
print(c.getPerimeter())
c.draw()
c.move(60, 40)
c.draw()
turtle.done()

        