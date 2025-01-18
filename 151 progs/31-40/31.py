#String Operations

my_list=[10,20]
print("Initial list",my_list)

my_list.append(30)
my_list.append(40)
print("After appending 30 and 40",my_list)

my_list.insert(1, 15)
print("After inserting 15 at index 1:", my_list)

my_list.remove(20)
print("After removing 20:", my_list)

popped_element = my_list.pop()
print(f"After popping the last element", (popped_element),":", my_list)

print("Final list:", my_list)