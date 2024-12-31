# n = int(input('n ='))
# for i in range (1, n+1):
#     print('*' * (i-1), end=" ")
#
#
#

# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#     return result
# print("Factorial of 5:", factorial(5))

# n = 5
# for i in range(1, n+1):
#     print("* " * i)


# list1= [x**2 for x in range(1,11)]
# print(list1)

# def fibonacci(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
#
# for i in range(10):
#     print(fibonacci(i), end=" ")

# nums = [1, 2, 3, 4]
# squared = list(map(lambda x: x ** 2, nums))
# print("Squared numbers:", squared)

class MyClass:
    @classmethod
    def class_method(cls):
        print("This is a class method")

    @staticmethod
    def static_method():
        print("This is a static method")

MyClass.class_method()
MyClass.static_method()