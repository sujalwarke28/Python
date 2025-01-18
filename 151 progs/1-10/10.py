#CAL SIMPLE INTEREST

principle_amt = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest: "))
no_of_years = float(input("Enter the time: "))

simple_interest = (principle_amt * rate_of_interest * no_of_years)/100

print(f"The interest is '{simple_interest}'")

total_amount = simple_interest + principle_amt
print(f"The total amount payable after interest is {total_amount}")