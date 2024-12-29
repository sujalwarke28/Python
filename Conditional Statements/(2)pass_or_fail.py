
marks1 = int(input('Enter your marks: '))
marks2 = int(input('Enter your marks: '))
marks3 = int(input('Enter your marks: '))

totalMarks=((marks1+marks2+marks3)/300)*100

if totalMarks>=40 and marks1 >= 33 and marks2 >= 33 and marks3 >=33:
    print("passed")
else:
    print('You fail')

print(totalMarks)

