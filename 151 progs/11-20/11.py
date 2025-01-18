#GREATEST NUMBER

num1 = int(input("Number 1 : "))
num2 = int(input("Number 2 : "))
num3 = int(input("Number 3 : "))

if num1 > num2 and num1 > num3:
    print(f"{num1} is the greatest number")
elif num2 > num1 and num2 > num3:
    print(f"{num2} is the greatest number")
else:
    print(f"{num3} is the greatest number")