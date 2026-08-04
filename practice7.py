#tic tac toe game made with function loop if else list logic this is two player game in my upcoming project u will see single player tic tac toe

import os

score = {"X": 0, "O": 0, "Draw": 0}

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def display():
    clear()
    print("\nTIC TAC TOE\n")
    print(f"X : {score['X']}   O : {score['O']}   Draws : {score['Draw']}\n")
    for r, ele in enumerate(lala):
        print(f"   {ele[0] if ele[0] else ' '}  |  {ele[1] if ele[1] else ' '}  |  {ele[2] if ele[2] else ' '}   ")
        if r < 2:
            print("  ---+-----+---")
    print()

def winner():
    for el in lala:
        if el[0] == el[1] == el[2] != "":
            return True
    for i in range(3):
        if lala[0][i] == lala[1][i] == lala[2][i] != "":
            return True
    if lala[0][0] == lala[1][1] == lala[2][2] != "" or lala[2][0] == lala[1][1] == lala[0][2] != "":
        return True
    return False

def get_input(prompt):
    while True:
        try:
            val = int(input(prompt))
            return val
        except ValueError:
            print("Please enter a number 0-2")

while True:
    lala = [
        ["", "", ""],
        ["", "", ""],
        ["", "", ""],
    ]
    player = "X"
    moves = 0

    while True:
        display()
        print(f"Player {player}'s turn")

        a = get_input("Enter row (0-2): ")
        b = get_input("Enter column (0-2): ")

        if (a > 2 or a < 0) or (b > 2 or b < 0):
            print("Invalid choice")
            input("Press Enter to continue...")
            continue
        elif lala[a][b] != "":
            print("That box is already filled")
            input("Press Enter to continue...")
            continue
        else:
            lala[a][b] = player
            moves += 1

        if winner():
            display()
            score[player] += 1
            print(f"Yayayaaaa Congratulationsss player {player} won the game!")
            break

        if moves == 9:
            display()
            score["Draw"] += 1
            print("The Match is Draw")
            break

        if player == "X":
            player = "O"
        else:
            player = "X"

    again = input("\nPlay again? (y/n): ").strip().lower()
    if again != "y":
        print(f"\nFinal Score -> X: {score['X']}  O: {score['O']}  Draws: {score['Draw']}")
        print("Thanks for playing!")
        break
    
