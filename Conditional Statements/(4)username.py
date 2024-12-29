name=input('Enter username: ')

if len(name) in range(0,4):
    print('too small')

elif len(name)>10:
    print('username too long')
else:
    print('appropriate')