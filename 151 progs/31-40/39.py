#Given two lists, find the common elements and store them in a new list.

x=int(input("Enter the number of elements you want in your list: "))

list1=[]
list2=[]


for i in range(0,x):
    z=input("Enter element for the list 1: ")
    list1.append(z)
print("")

for i in range(0,x):
    z=input("Enter element for the list 2: ")
    list2.append(z)
print("Your List 1",list1)
print("Your List 2 ",list2)


common_elements = list(set(list1) & set(list2))   # '&' is used for intersection between two sets
print("Common elements:", common_elements)
