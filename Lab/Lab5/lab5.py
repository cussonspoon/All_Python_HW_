import turtle
import math
import random

#Question 1
# print("Pattern A")
# for i in range(1, 6):
#     num = 1
#     while num <= i:
#         print(num , end = "")
#         num += 1
#     print('')

# print("Pattern B")
# for j in range(5, 0, -1):
#     num2 = 1
#     while num2 <= j:
#         print(num2 , end = "")
#         num2 += 1
#     print('')

#Question 2
# N = int(input("Enter rows and columns: "))
# ls = 100/N
# def square(ls):
#     for i in range(0, 4):
#         turtle.forward(ls)
#         turtle.right(90)
# turtle.showturtle()
# turtle.speed(0)
# for j in range(0, N+1):
#     for a in range(0, N):
#      square(ls)
#      turtle.forward(ls)
#     turtle.penup()
#     turtle.goto(0, 0)
#     turtle.setheading(270)
#     turtle.forward(ls*j)
#     turtle.setheading(0)
#     turtle.pendown()
# turtle.done()

#Question 3
# N = int(input("Enter rows and columns: "))
# ls = 100/N
# def square(ls):
#     for i in range(0, 4):
#         turtle.forward(ls)
#         turtle.right(90)
# turtle.showturtle()
# turtle.speed(0)
# for j in range(0, N+1):
#     for a in range(0, N):
#      if a % 2 == 0:
#       turtle.fillcolor("White")
#       turtle.begin_fill()
#       square(ls)
#       turtle.end_fill()
#       turtle.forward(ls)
#       turtle.fillcolor("Black")
#       turtle.begin_fill()
#       square(ls)
#       turtle.end_fill()
#       turtle.forward(ls)
#      else:
#       turtle.fillcolor("Black")
#       turtle.begin_fill()
#       square(ls)
#       turtle.end_fill()
#       turtle.forward(ls)
#       turtle.fillcolor("White")
#       turtle.begin_fill()
#       square(ls)
#       turtle.end_fill()
#       turtle.forward(ls)
#     turtle.penup()
#     turtle.goto(0, 0)
#     turtle.setheading(270)
#     turtle.forward(ls*j)
#     turtle.setheading(0)
#     turtle.pendown()
# turtle.done()

#Question 4
# for num in range(1, 50):
#  if num % 3 == 0:
#   continue
#  print(str(num), end = "")
#  if num < 49:
#   print(",", end = "")

#Question 5
# charc = input("Please enter a character: ")
# code = ord(charc)
# print(str(code))
# if code == 0x30 or 0x31 or 0x32 or 0x33 or 0x34 or 0x35 or 0x36 or 0x37 or 0x38 or 0x39:
#     print(str(charc), "is a numeric character.")
# elif code == 0x41 or 0x42 or 0x43 or 0x44 or 0x45 or 0x46 or 0x47 or 0x48 or 0x49 or 0x5:
#     print(str(charc), "is a capital letter and its small-case letter is" + charc.lower())

#Question 6
A = int(input("Enter an integer"))

if A % 2 == 0:
    for x in range(1, (A - (A // 2)) + 1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

    for x in range((A - (A // 2)), 0, -1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

if A % 2 != 0:
    for x in range(1,(A - ((A+1) // 2)) + 1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()

    for x in range((A - ((A-1) // 2)), 0, -1):
        num = 1
        row_values = []
        for y in range(x):
            row_values.append(num)
            num *= 2
        row_values.reverse()
        for value in row_values:
            print(value, end=" ")
        print()








 