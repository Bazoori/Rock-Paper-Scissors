import random
choices = ["rock", "paper", "scissors"]

while True:
    computer = random.choice(choices)
    player = input
    while player not in choices:
        player = input("Rock, Paper or Scissors?!: ").lower()

    print(f"computer has chosen: {computer}")
    print(f"player has chosen: {player}")

    if computer == player:
        print("Tie")
    elif (computer == "rock" and player == "scissors") or (computer == "paper" and player == "rock") or (computer == "scissors" and player == "paper"):
        print("You Lost! ")
    else:
        print("You Won!")

    play_again = input("Would you like to play another round?").lower()

    if play_again != "yes":
        break

print("Bye!")
