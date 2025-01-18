# Sum and avg of the numbers in the list

x=int(input("Enter the number of elements you want in your list: "))
numbers=[]
for i in range(0,x):
    z=input("Enter element for the list: ")
    numbers.append(z)
print("Your List",numbers)
z=list(map(float,numbers))

total = sum(z)
average = total / len(z)

# Print the results
print(f"Sum: {total}")
print(f"Average: {average}")