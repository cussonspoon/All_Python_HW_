
#Question 1
def list_number(n, lst, count=0):
    if count == len(lst):
        return False
    if n == lst[count]:
        return True
    return list_number(n, lst, count + 1)

print(list_number(2, [1, 2, 3]))
print(list_number(0, [1, 2, 3]))

#Question 2
def list_reverse(lst, count=None, result = None):
    if count is None:
        count = len(lst) - 1
    if result is None:
        result = []
    result.append(lst[count])
    if count == 0:
        return result
    return list_reverse(lst, count - 1, result)

print(list_reverse([1, 2, 3]))
print(list_reverse([5, 4, 3, 2, 1]))

#Question 3
def gcd(x, y):
    if y == 0:
        return x
    return gcd(y, x % y)

print(gcd(100, 15))

#Question 4
import turtle
turtle.speed(0)

def draw(x, y):
    if y == 0:
        turtle.dot(5)
        return
    turtle.forward(x)
    draw(x / 2, y - 1)
    turtle.backward(x * 2)
    draw(x / 2, y - 1)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    draw(x / 2, y - 1)
    turtle.backward(x * 2)
    draw(x / 2, y - 1)
    turtle.forward(x)
    turtle.right(90)
draw(100, 4)
turtle.mainloop()



#Question 5

def zerosum(lst, index=0, current_subset=None, result=None):
    if current_subset is None:
        current_subset = []
    if result is None:
        result = []
    if index == len(lst):
        if sum(current_subset) == 0 and len(current_subset) != 0:
            result.append(current_subset.copy())
        return
    current_subset.append(lst[index])
    zerosum(lst, index + 1, current_subset, result)
    current_subset.pop()
    zerosum(lst, index + 1, current_subset, result)
    if index == 0:
        if len(result) <= 1:
            return "No"
        else:
            return f"Yes {result}"
lst1 = [-7, -3, -2, 5, 7]
lst2 = [2, -3, 5, 8, 11, 23, -1]
print(zerosum(lst1))
print(zerosum(lst2))






    





    
    
    
