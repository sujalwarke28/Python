'''
A spam comment is defined as a text containing following keywords:
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
to detect these spams.
'''

msg=(input('Write a message: '))
p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe"
p4 = "click this"

if ((p1 in msg) or (p2 in msg) or (p3 in msg) or (p4 in msg)):
    print("This is a spam message")
else:
    print("This is not a spam")
