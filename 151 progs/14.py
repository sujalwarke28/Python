#sum of 1st N natural number from user

n = int(input("Enter a number: "))
sum = 0
if n >= 0:
    for i in range (1, n+1):
        sum += i
    print(sum)
else:
    print("Input a number greater than or equal to 0")