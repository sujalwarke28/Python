
a = int(input('Enter value of a: '))
b = int(input('Enter value of b: '))
c = int(input('Enter value of c: '))
d = int(input('Enter value of d: '))

print('Evaluating: \n')

if a > b and a > c and a>d:
    print(f'a={a} is the greatest number')

elif b>a and b>c and b>d:
    print(f'b={b} is the greatest number')

elif c>a and c>b and c>d:
    print(f'c={c} is the greatest number')

elif d>a and d>b and d>c:
    print(f'd={d} is the greatest number')
