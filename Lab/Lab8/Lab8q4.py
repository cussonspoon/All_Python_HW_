#Question 4
first = input("Enter your first name")
last = input("Enter you last name")
gender = input("Enter your gender(m/f)")

print(gender.upper() + last[0].upper() + first[0:6].upper())