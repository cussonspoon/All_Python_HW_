import turtle
#Question 1
def time24hourTo12hour(time24):
    hours, minutes = map(int, time24.split(':'))
    period = "AM" if hours < 12 else "PM"

    if hours > 12 :
        hours -= 12

    return f"{hours:02d}:{minutes:02d} {period}"

    
print(time24hourTo12hour("11:45"))
print(time24hourTo12hour("23:59"))

#Question 2
def calendar_of_2023(month):
    wn = turtle.Screen()
    wn.tracer(0)
    screen = turtle.Screen()
    screen.screensize(2000 ,10000)
    turtle.showturtle()
    turtle.speed(0)


    #Function for building template(Just reminding myself don't mind me)
    def template(n):
        if n == 1:
            turtle.write("                         January 2023")
        elif n == 2:
            turtle.write("                         Febuary 2023")
        elif n == 3:
            turtle.write("                         March 2023")
        elif n == 4:
            turtle.write("                         April 2023")
        elif n == 5:
            turtle.write("                         May 2023")
        elif n == 6:
            turtle.write("                         June 2023")
        elif n == 7:
            turtle.write("                         July 2023")
        elif n == 8:
            turtle.write("                         August 2023")
        elif n == 9:
            turtle.write("                         September 2023")
        elif n == 10:
            turtle.write("                         October 2023")
        elif n == 11:
            turtle.write("                         November 2023")
        elif n == 12:
            turtle.write("                         December 2023")
        turtle.penup()
        turtle.left(90)
        turtle.forward(10)
        turtle.pendown()
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(210)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.forward(210)
        turtle.right(90)
        turtle.forward(20)
        turtle.backward(20)
        turtle.setheading(0)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
        turtle.write(" Su      Mo      Tu      We      Th      Fr      Sa")
        turtle.right(90)
        turtle.forward(20)
        turtle.setheading(0)
        if n == 4 or n == 7 or n == 12 : 
            row = 7
        else : row = 6

        while row != 0 :
                for s in range(1, 8) :               
                    turtle.forward(30)
                    turtle.right(90)
                    turtle.forward(20)
                    turtle.right(90)
                    turtle.forward(30)
                    turtle.right(90)
                    turtle.forward(10)
                    turtle.right(90)
                    turtle.left(90)
                    turtle.forward(10)
                    turtle.right(90)
                    turtle.forward(30)
                turtle.backward(210)
                turtle.right(90)
                turtle.forward(20)
                turtle.setheading(0)           
                row -= 1
        turtle.left(90)
        turtle.forward(80)
        turtle.right(90)



    #Function for writing number(Just reminding myself don't mind me)
    def number(space, maxnum, nlnum, month4712) :
        num = 1
        turtle.forward(30*space)
        if month4712 == 1 :
            turtle.left(90)
            turtle.forward(20)
            turtle.setheading(0)
        while num <= maxnum : 
            turtle.write('   ' + str(num))
            turtle.forward(30)
            if num == nlnum or num == nlnum + 7 or num == nlnum + 7*2 or num == nlnum + 7*3 or num == nlnum + 7*4 :
                turtle.backward(210)
                turtle.right(90)
                turtle.forward(20)
                turtle.setheading(0)
            num += 1


    #Function for moving turtle to create another calendar(Just reminding myself don't mind me)
    def move(backward):
        turtle.backward(30*backward)
        turtle.right(90)
        turtle.forward(30)
        turtle.setheading(0)

    # #_______________________________________________________________________________________________________________________________________________________________

    # 1# Calendar
    if month == 1:
        template(1)
        turtle.penup()
        number(0, 31, 7, 0)

    # 2# Calendar
    if month == 2:
        turtle.penup()
        move(3)
        turtle.pendown()
        template(2)
        turtle.penup()
        number(3, 28, 4, 0)

    # 3# Calendar
    if month == 3:
        turtle.penup()
        move(3)
        turtle.pendown()
        template(3)
        turtle.penup()
        number(3, 31, 4, 0)

    # 4# Calendar
    if month == 4:
        turtle.penup()
        move(6)
        turtle.pendown()
        template(4)
        turtle.penup()
        number(6, 30, 1, 1)

    # 5# Calendar
    if month == 5:
        turtle.penup()
        move(1)
        turtle.pendown()
        template(5)
        turtle.penup()
        number(1, 31, 6, 0)

    # 6# Calendar
    if month == 6:
        turtle.penup()
        move(4)
        turtle.pendown()
        template(6)
        turtle.penup()
        number(4, 30, 3, 0)

    # 7# Calendar
    if month == 7:
        turtle.penup()
        move(6)
        turtle.pendown()
        template(7)
        turtle.penup()
        number(6, 31, 1, 1)

    # 8# Calendar
    if month == 8:
        turtle.penup()
        move(2)
        turtle.pendown()
        template(8)
        turtle.penup()
        number(2, 31, 5, 0)

    # 9# Calendar
    if month == 9:
        turtle.penup()
        move(5)
        turtle.pendown()
        template(9)
        turtle.penup()
        number(5, 30, 2, 0)

    # 10# Calendar
    if month == 10:
        turtle.penup()
        move(0)
        turtle.pendown()
        template(10)
        turtle.penup()
        number(0, 31, 7, 0)

    # 11# Calendar
    if month == 11:
        turtle.penup()
        move(3)
        turtle.pendown()
        template(11)
        turtle.penup()
        number(3, 30, 4, 0)

    # 12# Calendar
    if month == 12:
        turtle.penup()
        move(5)
        turtle.pendown()
        template(12)
        turtle.penup()
        number(5, 31, 2, 1)

    wn.update()
    wn.mainloop()

calendar_of_2023(8)

#Question 3
number = int(input("Enter a number"))
def firstdigit(n):
    if n == 0 :
        first = ""
    if n == 1 :
        first = "one"
    if n == 2 :
        first = "two"
    if n == 3 :
        first = "three"
    if n == 4 :
        first = "four"
    if n == 5 :
        first = "five"
    if n == 6 :
        first = "six"
    if n == 7 :
        first = "seven"
    if n == 8 :
        first = "eight"
    if n == 9 :
        first = "nine"
    return first

def tenthdigit(n):
    tenth = n // 10
    one = n % 10
    if tenth == 0:
        second = ""
    if tenth == 1 and one == 0:
        second = "ten"
    if tenth == 1 and one == 1:
        second = "eleven"
    if tenth == 1 and one == 2:
        second = "twelve"
    if tenth == 1 and one == 3:
        second = "thirteen"
    if tenth == 1 and one == 4:
        second = "fourteen"
    if tenth == 1 and one == 5:
        second = "fifteen"
    if tenth == 1 and one == 6:
        second = "sixteen"
    if tenth == 1 and one == 7:
        second = "seventeen"
    if tenth == 1 and one == 8:
        second = "eighteen"
    if tenth == 1 and one == 9:
        second = "nineteen"
    if tenth == 2:
        second = "twenty" + " " + firstdigit(one)
    if tenth == 3:
        second = "thirty" + " " + firstdigit(one)
    if tenth == 4:
        second = "fourty" + " " + firstdigit(one)
    if tenth == 5:
        second = "fifty" + " " + firstdigit(one)
    if tenth == 6:
        second = "sixty" + " " + firstdigit(one)
    if tenth == 7:
        second = "seventy" + " " + firstdigit(one)
    if tenth == 8:
        second = "eighty" + " " + firstdigit(one)
    if tenth == 9:
        second = "ninety" + " " + firstdigit(one)
    return second

def hundreddigit(n):
    hundredth = n // 100
    if hundredth == 1:
        third = "one hundred"
    if hundredth == 2:
        third = "two hundred"
    if hundredth == 3:
        third = "three hundred"
    if hundredth == 4:
        third = "four hundred"
    if hundredth == 5:
        third = "five hundred"
    if hundredth == 6:
        third = "six hundred"
    if hundredth == 7:
        third = "seven hundred"
    if hundredth == 8:
        third = "eight hundred"
    if hundredth == 9:
        third = "nine hundred"
    return third
        

if 100 <= number <= 999:
    if number % 100 == 0 :
        print(hundreddigit(number))
    elif 11 <=number % 100 <= 99 :
        print(hundreddigit(number) + " and " + tenthdigit(number%100))
    elif 1 <=number % 100 <= 9 :
        print(hundreddigit(number) + " and " + firstdigit(number%100))
elif 10 <= number <= 99:
    print(tenthdigit(number))
elif 0 <= number <= 9:
    print(firstdigit(number))
else :
    print("I don't know")

#Question 4
number = int(input("Input your amount of money: "))
while number >= 0 :
    if number // 1000 != 0 :
        thousand = number // 1000
        number %= 1000
    else:
        thousand = "0"
    if number // 500 != 0 :
        fivehundred = number // 500
        number %= 500
    else:
        fivehundred = "0"
    if number // 100 != 0 :
        hundred = number // 100
        number %= 100
    else:
        hundred = "0"
    if number // 50 != 0 :
        fifty = number // 50
        number %= 50
    else:
        fifty = "0"
    if number // 20 != 0 :
        twenty = number // 20
        number %= 500
    else:
        twenty = "0"
    if number // 10 != 0 :
        ten = number // 10
        number %= 10
    else:
        ten = "0"
    if number //2 != 0 :
        two = number // 2
        number %= 2
    else:
        two = "0"
    if number >= 0 :
        while number >= 0:
            one = 0
            number -= 1
            one += 1
    else:
        one = "0"
print("1000 baht notes: " + str(thousand))
print("500 baht notes: " + str(fivehundred))
print("100 baht notes: " + str(hundred))
print("50 baht notes: " + str(fifty))
print("20 baht notes: " + str(twenty))
print("10 baht coins: " + str(ten))
print("2 baht coins: " + str(two))
print("1 baht coins: " + str(one))

#Question 5
num = int(input("Enter number: "))
def reverse_integer(n):
    reversed_num = int(str(n)[::-1])
    return reversed_num
print("Reversed number:", reverse_integer(num))



        
        