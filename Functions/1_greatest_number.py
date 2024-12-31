#this belongs to chapter no 8 practice set
a = int(input('num: '))
b = int(input('num: '))
c = int(input('num: '))

def greatest(a,b,c):
    if (a>b) and (a>c):
        print('a is greatest')
    elif (b>a) and (b>c):
        print('b is greatest')
    else:
        print('c is greatest')
greatest(a,b,c)