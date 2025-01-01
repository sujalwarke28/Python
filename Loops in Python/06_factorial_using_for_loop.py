# w.a.p to calculate factorial using 'for' loop

n = int(input('Enter you number: '))

product = 1
for i in range(1,n+1):
    product=product*i

print (f"the factorial of {n} is {product}")


