#max and min in the list

x=int(input("Enter the number of elements you want in your list: "))
numbers=[]
for i in range(0,x):
    z=input("Enter element for the list: ")
    numbers.append(z)
print("Your List",numbers)

max_value = max(numbers)
min_value = min(numbers)

print(f"Maximum value: {max_value}")
print(f"Minimum value: {min_value}")