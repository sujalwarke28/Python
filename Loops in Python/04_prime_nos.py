# w.a.p to find prime nos

n = int(input('Enter a number: '))

for i in range(2,n):
    if n % i == 0:
        print(f"number '{n}' is not a prime number")
    else:
        print(f"number '{n}' is a prime number")
        break

