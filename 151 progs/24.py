# Check Prime (Function)

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):  # this represents (2, int(n+1)) just 1 is taken outisde parenthesis
        if n % i == 0:
            return False
    return True

# Test the function with user input
try:
    number = int(input("Enter a number to check if it's prime: "))
    if is_prime(number):
        print(f"{number} is a prime number.")
    else:
        print(f"{number} is not a prime number.")
except ValueError:
    print("Please enter a valid integer.")