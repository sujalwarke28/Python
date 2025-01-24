number = input("Enter a number: ")

if number.isdigit():
    if number == number[::-1]:
        print("The number is palindrome")
    else:
        print("The number is not palindrome")
else:
    print("Ener a valid number")