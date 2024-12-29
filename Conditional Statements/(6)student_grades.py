marks = int(input('Enter your marks: '))

if marks in range(90,101):
    print('Excellent')

elif marks in range(80,90):
    print('Grade A')

elif marks in range(70,80):
    print('Grade B')

elif marks in range(60,70):
    print('Grade C')

elif marks in range(50,60):
    print('Grade D')

else:
    print('Fail')

