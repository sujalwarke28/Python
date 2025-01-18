# WAP to print tables of inpput number

num = int(input("Enter a number: "))

for i in range(1, 11):
    print(f"{num} x {11-i} = {num *(11-i)}")
