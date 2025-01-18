# Prompt the user for an element and check if it exists in the tuple.

tuple1 = ('Chaitanya', 'Sourabh', 'Vinayak', 'shashank', 'Yash', 'Soham', 'Ronak', 'Sujal', 'Rohan', 'Tanishq')
element = input("Enter an element: ")
if element in tuple1:
    print("Element exists in the tuple.")
else:
    print("Element does not exist in the tuple.")