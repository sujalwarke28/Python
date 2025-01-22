# Number Guessing (While Loop)

# num = int(input("ENeter a number: "))
#
# number = 90
#
# if num == number:
#     print("Congrats, you are spot on")
#
# elif num < number:
#     if num >= (number - 10):
#         print("You are close, try a little higher")
#     else:
#         print("Nope, Try again")
#
# elif num > number:
#     if num <= (number + 10):
#         print("You are close, try a little lower")
#     else:
#         print("Nope, Try again")





import random


random_number = random.randint(1, 100)  # Generate a random number between 1 and 100

print("I have selected a random number between 1 and 100. Can you guess what it is?")


while True:      # Loop until the user guesses the correct number
    user_input = input("Enter your guess: ")

    # Check if the input is numeric
    if user_input.isdigit():
        user_guess = int(user_input)

        # Provide feedback based on the guess
        if user_guess < random_number:
            print("Too low! Try again.")
        elif user_guess > random_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed it right. The number was {random_number}.")
            break
    else:
        print("Please enter a valid number.")
