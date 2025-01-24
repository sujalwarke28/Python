# GCD

def gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Update a and b using the Euclidean algorithm
    return abs(a)  # Return the absolute value of the result

# Example usage:
num1 = int(input('Number: '))
num2 = int(input('Number: '))
print(f"The GCD of {num1} and {num2} is: {gcd(num1, num2)}")

