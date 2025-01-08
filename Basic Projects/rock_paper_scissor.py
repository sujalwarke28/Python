import random

choices = ["rock", "paper", "scissors"]
user = input("Enter rock, paper, or scissors: ").lower()
computer = random.choice(choices)
print(f"Computer chose: {computer}")

if user == computer:
    print("It's a tie!")
elif (user == "rock" and computer == "scissors") or (user == "scissors" and computer == "paper") or (user == "paper" and computer == "rock"):
    print("You win!")
else:
    print("You lose!")
