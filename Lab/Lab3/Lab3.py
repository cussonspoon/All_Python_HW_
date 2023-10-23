#Question 1
import math
print(int(math.pi))
print(format(math.pi, "6.4f"))
print(format(math.pi, "10.4e"))

#Question 2
char = input("Please enter a character: ")
code = ord(char)
pattern = "u" + format(code, "04x")
print("The Unicode of " + char + " is " + pattern)

#Question 3
first = input("Please enter the first string")
second = input("Please enter the second string")
third = input("Plase input the third string")
print("The whole string is: " + first.upper() + second.upper() + third.upper())
