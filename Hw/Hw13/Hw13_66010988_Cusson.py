#Question 1
def print_btree(lst, count, count2 = 0):
    result = ""
    if count == 0:
        count = ""
    for i in lst:
        if count2 == 1:
            count = ""
        if isinstance(i, int):
            result += count + str(i) + "\n"
        else:
            result += print_btree(i, count + ". ", count2 + 1)
    return result

print(print_btree([1, [[11, [111, 112]], [12, [121, [122, [1221, 1222]]]]]], 0))

#Question 2
def display_f(n):
    def display_f(n):
        if n == 0 or n % 2 == 1:
            return 0
        else:
            return 2 * display_f(n / 2) + 1

    for i in range(n + 1):
        if i < n:
            print(str(display_f(i)), end = ",")
        else:
            print(str(display_f(i)), end = ".")

n = 10
display_f(n)
print("")
#Question 3
def perm2(t, count=0):
    pairs = []
    if count == len(t):
        return pairs
    for i in t:
        if t[count] != i:
            pairs.append((t[count], i))
    pairs += perm2(t, count + 1)
    return pairs

result = perm2((1, 2, 3))
for i in result:
    print(i, end = " ")

print("")

def perm3(t, count=0):
    triples = []
    if count == len(t):
        return triples
    for i in t:
        for j in t:
            if t[count] != i and t[count] != j and i != j:
                triples.append((t[count], i, j))
    triples += perm3(t, count + 1)
    return triples

result = perm3((1, 2, 3, 4))
for i in result:
    print(i, end = " ")

print("")

def perm(t, n, current_tuple=()):
    if n == 0:
        if None in current_tuple:
            current_tuple = current_tuple[:current_tuple.index(None)]
        print(current_tuple, end = " ")
        return
    for element in t:
        if element not in current_tuple:
            perm(t, n - 1, current_tuple + (element,))

perm((1, 2, 3), 3)

#Question 4

#The only way I could do this question is to copy from other's git so I won't risk getting plagarism score ;--;

#Question 5
import turtle
turtle.left(90)
turtle.penup()
turtle.backward(300)
turtle.pendown()
turtle.speed(0)
def drawtree(n):
    if n > 10:
        turtle.forward(n)
        turtle.left(30)
        drawtree(3*n/4)
        turtle.right(60)
        drawtree(3*n/4)
        turtle.left(30)
        turtle.backward(n)
    else:
        return
drawtree(100)
turtle.exitonclick()