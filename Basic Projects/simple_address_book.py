address_book = {}

def add_contact(name, number):
    address_book[name] = number
    print("Contact added!")

def view_contacts():
    print("Contacts:")
    for name, number in address_book.items():
        print(f"{name}: {number}")

while True:
    print("\nOptions: 1. Add 2. View 3. Quit")
    choice = input("Enter choice: ")
    if choice == '1':
        name = input("Enter name: ")
        number = input("Enter number: ")
        add_contact(name, number)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        break
    else:
        print("Invalid choice!")
