#UNIQUE items in set

x=int(input("Enter the number of elements you want in your list: "))
numbers=[]
for i in range(0,x):
    z=input("Enter element for the list: ")
    numbers.append(z)
print("Your List",numbers)

unique_numbers = list(set(numbers))  # 'SET' function builds a set of unique elements only

# Print the result
print("List with duplicates removed:", unique_numbers)