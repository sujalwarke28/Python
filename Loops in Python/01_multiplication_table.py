#write a python program to print multiplication table using for loop

n = int(input('Enter the number: '))

for i in range(11):
    print(f"{n} x {i} = {n*i}")