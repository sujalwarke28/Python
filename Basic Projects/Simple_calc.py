def calculator():
    print("Select operation:")
    print("1. Add 2. Subtract 3. Multiply 4. Divide")
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ('1', '2', '3', '4'):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        if choice == '1':
            print(f"Result: {num1 + num2}")
        elif choice == '2':
            print(f"Result: {num1 - num2}")
        elif choice == '3':
            print(f"Result: {num1 * num2}")
        elif choice == '4':
            print(f"Result: {num1 / num2 if num2 != 0 else 'Error: Division by zero'}")
    else:
        print("Invalid Input")


calculator()