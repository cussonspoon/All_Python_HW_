#Question 1
def name_list():
    result = []
    count = 1
    while True:
        name = input(f"Enter name {count}: ")
        if name == "":
            break
        result.append(name)
        count += 1
    return result
# print(name_list())
        
#Question 2
list1 = [3,6,6,3,7,2,0,1,5,4]
def remove_the_third(list):
    num = 2
    while num < len(list):
        list.pop(num)
        num +=2
    return list
print(remove_the_third(list1))



#Question 3
def get_the_difference(list1, list2):
    result = []
    num1 = len(list1)
    num2 = len(list2)
    max = num1 if num1 >= num2 else num2
    for i in range(num1):
        if list1[i] in list2:
            continue
        else:
            result.append(list1[i])
    for i in range(num2):
        if list2[i] in list1:
            continue
        else:
            result.append(list2[i])
    return result
# print(get_the_difference([3,1,1,1,2,7], [4,1,1,2,2,5]))

#Question 4
import turtle 

turtle.speed(100)
turtle.penup()
turtle.goto(-200, 0)

def histogram(num_list):
    dic = {}
    for i in num_list:
        if i in dic: 
            dic[i] += 1
        else: 
            dic[i] = 1
    
    btw = 40
    tallest = max(dic.values())*20
    turtle.pendown()
    turtle.left(90)
    turtle.forward(tallest)
    turtle.penup()
    turtle.forward(10)
    turtle.write("Y", font=('Arial', 15, 'normal'))
    turtle.penup()
    turtle.goto(-200, 0)
    turtle.right(90)
    turtle.pendown()
    
    x = -200 + 20
    for key,value in dic.items():
        draw_bar(key, value*20, x, 0)
        turtle.pendown()
        turtle.forward(20)
        x += 20
    turtle.forward(20)
    turtle.write("X", font=('Arial', 15, 'normal'))
    turtle.hideturtle()
    
def draw_bar(key, value, x, y):
    turtle.goto(x, y)
    turtle.pendown()
    turtle.left(90)
    for i in range(2):
        turtle.forward(value)
        turtle.right(90)
        turtle.forward(20)
        turtle.right(90)
    turtle.right(90)
    turtle.penup()
    turtle.goto(x, y - 20)
    turtle.write(key, font=('Arial', 15, 'normal'))
    turtle.penup()
    turtle.goto(x, y)

histogram([1, 2, 2, 1, 3, 4, 5, 3, 4, 5, 4, 3, 5, 4, 5, 4, 5, 1, 4, 4, 3, 3, 4, 3, 3, 4, 4, 4, 6, 6, 6])
turtle.exitonclick()

    
#Question 5
def merge(list1, list2):
    merged = [i for i in list1]
    for i in list2:
        for m in merged: 
            if i < m: 
                merged.insert(merged.index(m), i)
                break
            elif i > m and merged.index(m) == len(merged) - 1:
                merged.append(i)
                break
    return merged                                                   

list1 = [1, 5, 16, 61, 111]
list2 = [2, 4, 5, 6]
print(merge(list1, list2))


