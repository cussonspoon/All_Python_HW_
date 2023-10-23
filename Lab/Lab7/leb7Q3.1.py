#Question 3.1
import turtle
class Rectangle:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def getArea(self):
        Area = self.__width*self.__height
        return Area
    
    def getPerimeter(self):
        P = self.__width*2 + self.__height*2
        return P
    
    def move(self, x, y):
        self.__x = x
        self.__y = y 

    def intersect(self, rec):
        a = [self.__x - self.__width/2, self.__y + self.__height/2]
        b = [self.__x + self.__width/2, self.__y + self.__height/2] 
        c = [self.__x + self.__width/2, self.__y - self.__height/2]
        d = [self.__x - self.__width/2, self.__y - self.__height/2] 
        e = [rec.__x - rec.__width/2, rec.__y + rec.__height/2]
        f = [rec.__x + rec.__width/2, rec.__y + rec.__height/2] 
        g = [rec.__x + rec.__width/2, rec.__y - rec.__height/2]
        h = [rec.__x - rec.__width/2, rec.__y - rec.__height/2] 
        
        if ((f[0] > a[0]) and (f[1] > c[1])) and (g[1] < b[1]) and (e[0] < b[0]):  
            new_width = min(b[0], f[0]) - max(a[0], e[0])
            new_height = min(b[1], f[1]) - max(c[1], g[1])
            return Rectangle(max(a[0], e[0]) + new_width/2, max(c[1], g[1]) + new_height/2, new_width, new_height)
        else:
            return None

    def draw(self):
        turtle.speed(4)
        turtle.setheading(0)
        turtle.penup()
        turtle.goto(self.__x, self.__y)
        turtle.pendown()
        turtle.forward(self.__width)
        turtle.right(90)
        turtle.forward(self.__height)
        turtle.right(90)
        turtle.forward(self.__width)
        turtle.right(90)
        turtle.forward(self.__height)




A = Rectangle(0, 0, 100, 200)
B = Rectangle(-200, 0, 100, 100)

A.draw()
B.draw()

C = A.intersect(B) #None
try:
    C.draw()
except Exception as x :
    print(x)

D = Rectangle(-50, -50, 200, 50)
D.draw()

E = A.intersect(D)
turtle.fillcolor("yellow")
turtle.begin_fill()
E.draw()
turtle.end_fill()

E.move(-100, 100)
turtle.begin_fill()
E.draw()
turtle.end_fill()

turtle.done()