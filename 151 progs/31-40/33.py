# 2nd LArgest value in the set

x=int(input("Enter the number of elements you want in your list: "))
numbers=[]
for i in range(0,x):
    z=input("Enter element for the list: ")
    numbers.append(z)
print("Your List",numbers)

numbers.sort()
second_largest = numbers[-2]

print(f"The second largest element is: {second_largest}")