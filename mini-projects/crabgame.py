import random
import time

print(
    "Welcome to Crab Game!\nA game about a crab living in a hut on the beach.\nThis crab really loves to collect things."
)
print(
    "You can find fun little things by looking around on the beach, or by digging into the sand."
)
print(
    "But be careful, every 61 seconds, a huge wave comes around, which would hurt you, so you only have 60 seconds to search before going back to your hut."
)
print("Do you think you have what it takes to be this crab?")

LSTUFF = ["sand", "shell", "crab", "fish", "mussel", "coin"]
DSTUFF = ["shell", "shiny rock", "worm", "pearl", "coin", "necklace", "ring", "glass"]

while True:
    play = input(
        "Type something in to start your new life as a crab. If you're too scared, just press Enter to exit.\n"
    )
    if play:
        game_running = True
        inventory: dict[str, int] = {}
        start_time = time.time()
        print("You wake up, another beautiful day of collecting stuff ahead of you!")
        break
    else:
        exit()


while game_running == True:
    elapsed_time = time.time() - start_time
    score = sum(inventory.values())
    score = int(score)
    try:
        with open("saves.txt", "r") as file:
            previous = int(file.read().strip())
    except FileNotFoundError:
        with open("saves.txt", "w") as file:
            file.write("0")
            previous = 0
    if elapsed_time > 60:
        print("The wave is coming, you better run!")
        print("...\n")
        print(
            "You barely managed to get back to your hut, now you can go over your findings."
        )
        print(f"Your score:{score}")
        print("All the Stuff you collected:")
        for item, amount in sorted(inventory.items()):
            print(f"-{item.capitalize()}: {amount}")
        if score > previous:
            print(
                f"This was a new highscore! You beat your old score {previous} by {score-previous} with your new score of {score}.\nCongratulations!"
            )
        else:
            print(
                f"You didn't beat your old score of {previous}. But you still did well with your score of {score}"
            )
        break

    if score > previous:
        with open("saves.txt", "w") as file:
            file.write(str(score))
            print(f"New High Score! {score} (Previous: {previous})")
    else:
        print(f"Your score: {score}. Previous high score: {previous}.")
    player_action = input(
        f"What would you like to do?\n[C] Check Inventory\n[L] Look around\n[D] Dig for stuff\n[G] Give up\nBut be careful, it's already been {int(elapsed_time)} seconds!\n>>> "
    ).lower()
    options = [
        "c",
        "l",
        "d",
        "g",
    ]
    if player_action not in options:
        print("You dont have any other options, please try again")
    elif player_action == "c":
        if inventory:
            print("\nYour Inventory")
            for item, amount in sorted(inventory.items()):
                print(f"-{item.capitalize()}: {amount}")
        else:
            print("\nYou dont dont own anything.")
    elif player_action == "l":
        if random.randrange(1, 11) > 5:
            amount_l = 1
            if random.randrange(1, 21) > 15:
                amount_l = 5
            stuff_player = random.choice(LSTUFF)
            print(f"Congratulations! You found:{amount_l} {stuff_player}")
            if stuff_player in inventory:
                inventory[stuff_player] += amount_l
            else:
                inventory[stuff_player] = amount_l
        else:
            print("You sadly didn't find anything.")
    elif player_action == "d":
        if random.randrange(1, 11) > 2:
            amount_d = 1
            if random.randrange(1, 21) > 10:
                amount_d = 5
            stuff_player = random.choice(DSTUFF)
            print(f"Congratulations! You found:{amount_d} {stuff_player}")
            if stuff_player in inventory:
                inventory[stuff_player] += amount_d
            else:
                inventory[stuff_player] = amount_d
        else:
            print("You sadly didn't find anything.")
    elif player_action == "g":
        print("You run away to your hut, before the wave was even visible.")
        print(f"Your score:{score}")
        print("All the Stuff you collected:")
        for item, amount in sorted(inventory.items()):
            print(f"-{item.capitalize()}: {amount}")
        if score > previous:
            print(
                f"This was a new highscore! You beat your old score {previous} by {score-previous} with your new score of {score}.\nCongratulations!"
            )
        else:
            print(
                f"You didn't beat your old score of {previous}. But you still did well with your score of {score}"
            )
        break
