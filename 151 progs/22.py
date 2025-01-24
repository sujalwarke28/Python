#Base, exponenet

def power(base, exponent):
    result = 1

    if exponent < 0:       # Handle negative exponents
        base = 1 / base
        exponent = -exponent


    for i in range(exponent):    # Calculate power using a loop
        result *= base

    return result


# Test the function
base = float(input("Enter the base: "))
exponent = int(input("Enter the exponent: "))
print(f"{base} to the power of {exponent} is {power(base, exponent)}")