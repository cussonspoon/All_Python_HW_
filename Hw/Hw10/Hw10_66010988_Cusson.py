import matplotlib.pyplot as plt
import numpy as np
#Question 1
def piechart(data_lst):
    unique_numbers = list(set(data_lst))
    result = [data_lst.count(num) for num in unique_numbers]
    y = np.array(result)
    plt.pie(y)
    plt.show()
piechart([3, 1, 3, 3, 2, 3, 3, 2, 3, 2, 4, 3, 3, 3, 3, 4, 3, 4, 3, 3, 3, 4, 3])

#Question 2
def bubble_sort(lst):
    n = len(lst)
    for i in range(n):
        for j in range(i+1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst
print(bubble_sort([3, 2, 9, 7, 8]))

#Question 3
list1 = [3,1,2,7]
list2 = [4,1,2,5]
def my_union(list1, list2):
    result = []
    for i in list1:
        result.append(i)
    for i in list2:
        if i not in list1:
            result.append(i)
    return result

def my_intersection(list1, list2):
    result = []
    for i in list1:
        if i in list2:
            result.append(i)
    return result

def my_difference(list1, list2):
    result = []
    for i in list1:
        if i not in list2:
            result.append(i)
    return result

print(my_union(list1, list2))
print(my_intersection(list1, list2))
print(my_difference(list1, list2))

#Question 4
def print_table(data):
    headers = data[0]
    max_widths = [len(str(header)) for header in headers]

    for row in data[1:]:
        for i, item in enumerate(row):
            max_widths[i] = max(max_widths[i], len(str(item)))

    for i, header in enumerate(headers):
        print(f"{header:<{max_widths[i]}}", end=" ")
    print("")

    for row in data[1:]:
        for i, item in enumerate(row):
            print(f"{item:<{max_widths[i]}}", end=" ")
        print("")

print_table([["X", "Y"], [0, 0], [10, 10], [200, 200]])
print_table([["ID", "Name", "Surname"], ["001", "Guido", "van Rossum"], ["002", "Donald", "Knuth"], ["003", "Gordon", "Moore"]])

#Question 5
def is_anagram(word1, word2):
    charword1 = [i for i in word1]
    charword2 = [i for i in word2]
    for i in charword1:
        if i in charword2:
            continue
        else:
            return False
    if len(charword1) != len(charword2):
        return False
    return True
print(is_anagram("silent", "listen"))
print(is_anagram("True", "Truea"))


        


