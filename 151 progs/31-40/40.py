
#Given two lists of equal length, create a third list that stores the element-wise sum.

num = int(input("Enter the number of elements you want in your list: "))

list1 = []
list2 = []

for i in range(0, num):
    z = int(input("Enter element for the list 1: "))
    list1.append(z)

print("")

for i in range(0, num):
    z = int(input("Enter element for the list 2: "))
    list2.append(z)

print("Your List 1", list1)
print("Your List 2", list2)

# Create sum_list using list comprehension
sum_list = [x + y for x, y in zip(list1, list2)]

print("Sum of elements:", sum_list)