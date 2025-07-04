import random


def print_game_state(fields: list[str]) -> None:
    print(
        """
{0}|{1}|{2}
{3}|{4}|{5}
{6}|{7}|{8}
    """.format(
            *fields
        )
    )


def winning(fields: list[str]) -> int:
    fields_string = "".join(fields)
    row1 = fields_string[0:3]
    row2 = fields_string[3:6]
    row3 = fields_string[6:9]
    col1 = fields_string[0] + fields_string[3] + fields_string[6]
    col2 = fields_string[1] + fields_string[4] + fields_string[7]
    col3 = fields_string[2] + fields_string[5] + fields_string[8]
    dia1 = fields_string[0] + fields_string[4] + fields_string[8]
    dia2 = fields_string[2] + fields_string[4] + fields_string[6]
    rows = [row1, row2, row3, col1, col2, col3, dia1, dia2]
    for x in rows:
        if "xxx" in x:
            print("The bot has won!\n")
            print_game_state(fields)
            return -1
        if "ooo" in x:
            print("You have won!\n")
            print_game_state(fields)
            return 1
    if " " not in fields_string:
        print("No one won!\n")
        print_game_state(fields)
        return 0
    return 2


def main() -> None:
    fields = list(" " * 9)
    playing = False

    start = input("Do you want to play TicTacToe? Type anything if yes.\n")
    if start:
        playing = True
        while playing:
            print_game_state(fields)

            while True:
                try:
                    player_choice = int(
                        input("Where do you want to place your circle?\n")
                    )
                except ValueError:
                    print("Only numbers, try again.\n")
                    continue
                options = range(0, 9)
                if player_choice in options:
                    if fields[player_choice] == " ":
                        fields[player_choice] = "o"
                        break

                    else:
                        print("That space is occupied.\n")

            if winning(fields) != 2:
                exit()

            while True:
                bot_choice = random.choice(options)
                if fields[bot_choice] == " ":
                    fields[bot_choice] = "x"
                    break

            if winning(fields) != 2:
                exit()
    else:
        print("Why did you even start?\n")
        exit()


if __name__ == "__main__":
    main()
