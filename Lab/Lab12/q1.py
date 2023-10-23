phone_book = {}

def add_contact(name, number):
    if name in phone_book:
        print(f"{name} is already in the phone book.")
    else:
        phone_book[name] = number

def remove_contact(name):
    if name in phone_book:
        del phone_book[name]
    else:
        print(f"{name} isn't in the book")

def find_contact(name):
    if name in phone_book:
        print(f"{name}: {phone_book[name]}")
    else:
        print(f"{name} isn't in the book.")

def print_contacts():
    print("Phone Book:")
    for name, number in phone_book.items():
        print(f"{name}: {number}")

while True:
    print("\nAdd contact (+)")
    print("Remove contact (-)")
    print("Find contact (f)")
    print("Print out contacts (p)")
    print("Quit (q)")

    choice = input("")

    if choice == "+":
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)
    elif choice == "-":
        name = input("Enter name: ")
        remove_contact(name)
    elif choice == "f":
        name = input("Enter name: ")
        find_contact(name)
    elif choice == "p":
        print_contacts()
    elif choice == "q":
        break
    else:
        print("Invalid choice")
