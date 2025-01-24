#Fibonacci Series

'''
0,1,1,2,3,5,8,13,21,34,55,89,144,...........
starts from 0
every number is sumed is the previous number
'''


def fibonacci(n):
    if n <= 0:
        return []  # Return an empty list for invalid input
    elif n == 1:
        return [0]  # Return the first Fibonacci number
    elif n == 2:
        return [0, 1]  # Return the first two Fibonacci numbers

    fib_list = [0, 1]  # Start with the first two numbers in the series
    for i in range(2, n):
        next_number = fib_list[-1] + fib_list[-2]  # Sum of the last two numbers
        fib_list.append(next_number)
    return fib_list


# Example usage:
n = int(input("Enter a number:" ))
print(f"The first {n} Fibonacci numb ers are: {fibonacci(n)}")



