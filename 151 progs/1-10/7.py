#WAP TO PRINT 2 PEINT DIAMOND STAR PATTERN

n = int(input("Enter a number: "))

for i in range(1, n+1):
    print(" "*(n-i) + "*" * i)
for i in range(n-1, 0, -1):
    print(" "*(n-i) + "*" * i)

















