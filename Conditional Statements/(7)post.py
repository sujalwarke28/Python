# METHOD 1

'''msg = str(input('Enter a post: '))

if "Sujal" or "sujal" in msg:
    print("This is talking about Sujal")
else:
    print('This is not about Sujal')
'''

# METHOD 2
msg = str(input('Enter a post: '))

if "Sujal".lower() in msg.lower():
#LOGIC : *.lower()* will convert the predefined string in lowercase and also the userinput to lowercase no what how it
#          was enetered initially, so it can take All CAPS, Snakecase or lowercase as input and still give a valid output
    print("This is talking about Sujal")
else:
    print('This is not about Sujal')
