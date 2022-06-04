import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

while True:
    user_pick = input("Enter either of rock, paper, scissors or type Q to quit. ").lower()
    if user_pick == "q":
        break
    if user_pick not in options:
        print("Not a valid choice. Enter your choice among rock, paper or scissors")
        continue

    # random_number = random.randint(0, 2)
    # computer_pick = options[random_number]
    computer_pick = random.choice(options)
    print("Computer picked", computer_pick + ".")

    if user_pick == "rock" and computer_pick == "scissors":
        print("You win!")
        user_wins += 1
    elif user_pick == "paper" and computer_pick == "rock":
        print("You win!")
        user_wins += 1
    elif user_pick == "scissors" and computer_pick == "paper":
        print("You win!")
        user_wins += 1
    elif user_pick == computer_pick:
        print("It's a tie. No one wins!")
    else:
        print("You lost :(")
        computer_wins += 1

print("You won", user_wins, "times.")
print("Computer won", computer_wins, "times.")
print("Goodbye. Have a nice day!")
