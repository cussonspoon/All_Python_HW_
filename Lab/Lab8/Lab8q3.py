#Question 3
short = input("Enter a short string")
long = input("Enter a long string")

vec1 = []
vec2 = []

for c1 in short:
    vec1.append(c1)
for c2 in long:
    vec2.append(c2)

count = 0
for sub in range(len(vec1)):
    for real in range(len(vec2)):
        if vec1[sub] == vec2[real]:
            count += 1
            break
if count == len(vec1):
    print("The short string is a substring of the long one")
else:
    print("The short string isn't a substring of the long one")
