def find_duplicates(dict):
    result = {}
    duplicates = {}

    for key, value in dict.items():
        if value in duplicates:
            if value not in result:
                result[value] = [duplicates[value]]
            result[value].append(key)
        else:
            duplicates[value] = key
    
    new = {}

    for value, keys in result.items():
        for key in  keys:
            new[key] = value

    return new

myDict = {
    "s5301" : "Fred", "s5302" : "Harry", "s5303" : "John", "s5304" : "Fred", "s5305" : "Harry"
}
print(find_duplicates(myDict))