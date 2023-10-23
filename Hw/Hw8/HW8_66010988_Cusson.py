#Question 1
def question1():
    n = int(input("Enter integer for conversion: "))
    binary = ""
    count = 0
    sum = 0
    if n == 0 :
        print("It is a 0")
    elif n < 0:
        print("It is negative")
    else:
        dividant = n
        while dividant*2 // 2 != 0:
            remainder = str(dividant % 2)
            binary = remainder + binary
            dividant //= 2
        print("The binary code is: " + binary)
        for i in range(1, len(binary) + 1):
            pos = binary[-i]
            sum += 2**count*int(pos)
            count += 1
        print("The binary when converted back is: " + str(sum))
        
#Question 2
def question2():
    result = ""
    alphabetlow = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alphabetup = [i.upper() for i in alphabetlow]
    alphabet = alphabetlow + alphabetup
    word = input("Enter some text: ")
    for char in alphabet:
        x = word.count(char)
        if x != 0:
            prob = str("{:.2f}".format((x/len(word))*100)) + "%"
            result += char + "    " + prob + "\n"
    print("-- Character Frequency Table --")
    print("char percantage (character count / string length)")
    print(result)

#Question 3
def question3():
    import turtle
    result = []
    count = []
    alphabetlow = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    alphabetup = [i.upper() for i in alphabetlow]
    alphabet = alphabetlow + alphabetup
    word = input("Enter some text: ")
    for char in alphabet:
        x = word.count(char)
        if x != 0:
            result.append(char)
            count.append(int(x))
    turtle.screensize(2000, 2000)
    t = turtle.Turtle()
    t2 = turtle.Turtle()
    t.speed(0)
    t2.speed(0)
    t2.left(90)
    t2.forward(max(count)*20)
    def graph(n, char):
        t.forward(20)
        t.left(90)
        t.forward(n*20)
        t.right(90)
        t.forward(10)
        t.right(90)
        t.forward(n*20)
        t.right(90)
        t.forward(10)
        t.backward(10)
        t.left(90)
        t.penup()
        t.forward(15)
        t.write(char)
        t.backward(15)
        t.pendown()
        t.setheading(0)
    for i in range(len(count)):
        graph(count[i], result[i])

    t.forward(20)
    turtle.done()

#Question 4
def question4():
    vec = []
    count = 1
    sum = 0
    while True:
        try:
            while True:
                n = input("Enter the first 9 digits of an ISBN-10 as a string: ")
                check = int(n)
                if len(n) != 9:
                    print("The input isn't a 9 digits.")
                    continue
                else: 
                    break
            for i in n:
                vec.append(int(i))
            for j in range(9):
                sum += vec[j]*count
                count += 1
            lastd = sum % 11
            if lastd == 10:
                lastd = "X"
            result = n + str(lastd)
            print("Your ISBN-10 number is " + result)
            break
        except:
            print("Enter 9 digits string")
            continue

question1()
question2()
question3()
question4()