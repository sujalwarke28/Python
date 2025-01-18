#LCM

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return abs(a)

def lcm(a, b):
    if a == 0 or b == 0:
        return 0  # LCM is 0 if either number is 0
    return abs(a * b) // gcd(a, b)

# Example usage:
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print(f"The LCM of {num1} and {num2} is: {lcm(num1, num2)}")