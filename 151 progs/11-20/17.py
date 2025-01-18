#COUNT NUMBER OF DIGITS

number = input("Enter a number: ")
num = str(number)
print(len(num))

'''
number = input("Enter a number: ")

if number.lstrip('-').isdigit():  #checks if the number s valif and if number is -ve, doesnot count '-' symbol
    digit_count = len(number.lstrip('-'))
    print(f"The number {number} has {digit_count} digit(s).")
else:
    print("Please enter a valid integer.")

'''