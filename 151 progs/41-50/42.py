#Convert a user-defined tuple to a list, modify it, and convert it back to a tuple.

tuple1 = input("Enter a tuple: ")
list1 = list(tuple1)
print('Modified list:', list1)

# list1[0] = "Chaitanya"
tuple1 = tuple(list1)

print("Modified tuple:", tuple1)