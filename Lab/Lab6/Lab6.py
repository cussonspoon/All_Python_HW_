import turtle
#Question1
num = eval(input("Enter student's grade"))
def getgrade(num):
    if num >= 80 and num <= 100:
        grade = "A"
    if num >= 70 and num < 80:
        grade = "B"
    if num >= 60 and num < 70:
        grade = "C"
    if num >= 50 and num < 60:
        grade = "D"
    if num < 50 and num >= 0:
        grade = "F"
    else :
        grade ="invalid"
    return grade
print("A student grade is " + getgrade(num))

# #Question 2
X = int(input("Enter length of the square"))
length = X*8
turtle.speed(0)
def square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.right(90)
def loopsquare(X):
    square(length)
    turtle.forward(length/2)
    turtle.right(90)
    turtle.penup()
    turtle.forward(X)
    turtle.right(90)
    turtle.forward(length/2-X)
    turtle.setheading(0)
    turtle.pendown()
    square(length-X*2)
    turtle.penup()
    turtle.forward((length-X*2)/2)
    turtle.right(90)
    turtle.forward(X)
    turtle.right(90)
    turtle.forward(length/2-X)
    turtle.setheading(0)
    turtle.forward(X)
    turtle.pendown()
    square(length-X*4)
    turtle.penup()
    turtle.forward(X)
    turtle.right(90)
    turtle.forward(X)
    turtle.setheading(0)
    turtle.pendown()
    square(length-X*6)
    turtle.penup()
    turtle.home()
    turtle.forward(length/2)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(length)
    turtle.penup()
    turtle.home()
    turtle.right(90)
    turtle.forward(length/2)
    turtle.left(90)
    turtle.pendown()
    turtle.forward(length)
    turtle.backward(length/2)
loopsquare(X)
turtle.done()

#Question 3
def draw_polygon(x=0, y=0, side=4, size=100):
    turtle.speed(0)
    turtle.showturtle()
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(side):
        turtle.right(360/side)
        turtle.forward(size)
draw_polygon(0, 0)
draw_polygon(10, 10, 5)
draw_polygon(10, 10, 6, 150)
turtle.done()

#Question 4
def sum_of_digits(n):
    new = []
    for x in str(n):
        new.append(int(x))
    result = sum(new)
    return result
print(sum_of_digits(234))




