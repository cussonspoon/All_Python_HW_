s = frozenset([1, 2, 3])
def powerset(s):
    lst = list(s)
    n = len(lst)
    powerset = []

    for i in range(1 << n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(lst[j])
        powerset.append(frozenset(subset))

    return powerset

print(powerset(s), end = "")




