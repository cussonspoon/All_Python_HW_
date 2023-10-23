#Question 1
import turtle
import math
p0x = int(input("Enter cord-x for p0"))
p0y = int(input("Enter cord-y for p0"))
p1x = int(input("Enter cord-x for p1"))
p1y = int(input("Enter cord-y for p1"))
p2x = int(input("Enter cord-x for p2"))
p2y = int(input("Enter cord-y for p2"))
d02 = math.sqrt((p2x - p0x)**2 + (p2y - p0y)**2)
d12 = math.sqrt((p2x - p1x)**2 + (p2y - p1y)**2)
if p0x > p1x:
 is_left = True
else : is_left = False

turtle.showturtle()
turtle.penup()
turtle.goto(p0x, p0y)
turtle.write("p0(" + str(p0x) + "," + str(p0y) + ")")
turtle.pendown()
turtle.goto(p2x, p2y)
turtle.goto(p1x, p1y)
turtle.write("p1(" + str(p1x) + "," +  str(p1y) + ")")
turtle.penup()
turtle.goto(p2x, p2y)
turtle.hideturtle()
if is_left :
 if d02 < d12 : turtle.write("p2 is on the right side which is the side of p0");print("p2 is on the right side which is the side of p0")
 elif d02 > d12 : turtle.write("p2 is on the left side which is the side of p1");print("p2 is on the left side which is the side of p1")
 elif d02 == d12 : turtle.write("p2 is between p0 and p1");print("p2 is between p0 and p1")

else :
 if d02 < d12 : turtle.write("p2 is on the left side which is the side of p0");print("p2 is on the left side which is the side of p0")
 elif d02 > d12 : turtle.write("p2 is on the right side which is the side of p1");print("p2 is on the right side which is the side of p1")
 elif d02 == d12 : turtle.write("p2 is between p0 and p1");print("p2 is between p0 and p1")
turtle.done()

#Question 2
r1x = int(input("Enter a cord-x for the first rectangle"))
r1y = int(input("Enter a cord-y for the first rectangle"))
w1 = int(input("Enter a width for the first rectangle"))
h1 = int(input("Enter a height for the first rectangle"))
r2x = int(input("Enter a cord-x for the second rectangle"))
r2y = int(input("Enter a cord-y for the second rectangle"))
w2 = int(input("Enter a width for the second rectangle"))
h2 = int(input("Enter a height for the second rectangle"))

r1tpx = r1x + w1/2
r1tpy = r1y + h1/2
r1bpx = r1x - w1/2
r1bpy = r2y - h1/2

r2tpx = r2x + w2/2
r2tpy = r2y + h2/2
r2bpx = r2x - w2/2
r2bpy = r2y - h2/2

turtle.showturtle()
#First rec
turtle.penup()
turtle.goto(r1x, r1y)
turtle.forward(w1/2)
turtle.left(90)
turtle.pendown()
turtle.forward(h1/2)
turtle.left(90)
turtle.forward(w1)
turtle.left(90)
turtle.forward(h1)
turtle.left(90)
turtle.forward(w1)
turtle.left(90)
turtle.forward(h1/2)
#Second rec
turtle.penup()
turtle.goto(r2x, r2y)
turtle.forward(w2/2)
turtle.left(90)
turtle.pendown()
turtle.forward(h2/2)
turtle.left(90)
turtle.forward(w2)
turtle.left(90)
turtle.forward(h2)
turtle.left(90)
turtle.forward(w2)
turtle.left(90)
turtle.forward(h2/2)
turtle.penup()
def is_overlap():
    if r1tpx < r2bpx or r1tpy < r2bpy:
     turtle.write("No overlap")
    elif r1bpx > r2tpx or r1bpy > r2tpy:
     turtle.write("No overlap")
    else:
     turtle.write("There is an overlap")
is_overlap()
turtle.done()
