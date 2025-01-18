#No of chars in a string

string = input("Enter a phrase: ")
stringWithOutSpaces = string.replace(" ", "")
print("The no.of characters in string is: ", len(stringWithOutSpaces))