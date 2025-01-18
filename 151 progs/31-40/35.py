#Count no.of +ve, -ve and zeros

x=int(input("Enter the number of elements you want in your list: "))

numbers=[]

for i in range(0,x):
    z=input("Enter element for the list: ")
    numbers.append(z)
print("Your List",numbers)

z=list(map(float,numbers))

positive_count = 0
negative_count = 0
zero_count = 0

for num in z:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Positive numbers: {positive_count}")
print(f"Negative numbers: {negative_count}")
print(f"Zeros: {zero_count}")