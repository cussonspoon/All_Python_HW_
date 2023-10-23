def inverse(dic):
    result = dict()
    for key, value in dic.items(): 
        if value not in result: 
            result[value] = [key]
        else:
            result[value].append(key)
    return result

myDic = {'a':1, 'b':2, 'c':1, 'd':3, 'e':2, 'f':2}
print(inverse(myDic))