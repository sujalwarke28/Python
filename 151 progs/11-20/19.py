#SUM OF EVEN AND ODD NOS

number = int(input("Enter the range: "))
sum_even = 0
sum_odd = 0

for i in range(1, number+1):
    if i % 2 == 0:
        sum_even += i
    else:
        sum_odd += i


print(f"Sum of even numbers: {sum_even}")
print(f"Sum of odd numbers: {sum_odd}")


