#Write four functions: add(a, b), subtract(a, b), multiply(a, b), and divide(a, b). Then prompt the user for two numbers and the operation. Use the corresponding function to output the result.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is undefined."


print("What do you want to do ? : 1.add, 2.subtract, 3.multiply, 4.divide")

# Prompt the user for input
operation = input("Enter the operation: ")
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Validate the numbers
if num1.replace('.', '', 1).isdigit() and num2.replace('.', '', 1).isdigit():    
    num1 = float(num1)
    num2 = float(num2)

    # Perform the chosen operation
    if operation == "1":
        result = add(num1, num2)
    elif operation == "2":
        result = subtract(num1, num2)
    elif operation == "3":
        result = multiply(num1, num2)
    elif operation == "4":
        result = divide(num1, num2)
    else:
        result = "Invalid operation."

    print(f"Result: {result}")
else:
    print("Please enter valid numbers.")