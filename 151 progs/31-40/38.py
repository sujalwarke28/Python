#Write a function to reverse a given list in place.

x=int(input("Enter the number of elements you want in your list: "))

my_list=[]

for i in range(0,x):
    z=input("Enter element for the list: ")
    my_list.append(z)
print("Your List",my_list)

print("Reversed List",my_list[::-1])
