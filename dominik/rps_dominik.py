import random

CHOICES = {"r": "Rock", "p": "Paper", "s": "Scissors"}

print("Welcome to Rock, Paper, Scissors!")

rounds = 0
points_player = 0
points_bot = 0

while True:
    player_choice = input("Enter a choice [r/p/s]\n >>> ").lower()
    if player_choice not in CHOICES:
        print("Invalid choice. Please try again.")
    bot_choice = random.choice(list(CHOICES.keys()))

    print(f"You chose: {CHOICES[player_choice]}")
    print(f"The bot chose: {CHOICES[bot_choice]}")

    rounds += 1
    if player_choice == bot_choice:
        print("Draw!")

    won = False
    if player_choice == "r" and bot_choice == "s":
        won = True
    elif player_choice == "p" and bot_choice == "r":
        won = True
    elif player_choice == "s" and bot_choice == "p":
        won = True

    if won:
        points_player += 1
        print("You won!")
    else:
        points_bot += 1
        print("You lost!")

    print(f"Points: {points_player}:{points_bot}")

    if points_player > 2 or points_bot > 2:
        points_bot = points_player = 0
        if points_player > 2:
            print("You won the entire game! Well done.")
        else:
            print("The bot was just better, nice try.")
        play_again = input("Do you want to play again? [y/N]\n >>> ").lower()
        if play_again != "y":
            print("Goodbye.")
            break
