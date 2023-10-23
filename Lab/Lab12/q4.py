def is_subset(set1, set2):
    for i in set1:
        if i not in set2:
            return False
    return True

sup = set([1, 2, 3, 4])
sub = set([1, 2, 4])
print(is_subset(sub, sup))

sub = set([1, 2, 5])

print(is_subset(sub, sup))
            
