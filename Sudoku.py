import requests
import string

url = "https://api.api-ninjas.com/v1/sudokugenerate?difficulty=medium&width=3&height=3"

headers = {
    "X-Api-Key": "qRVMdtqb1nzwkOxTaMetnne4hUbd4fujCPhnsPf2"
}

a = requests.get(url, headers=headers)
data = a.json()

def display():
    print("   1 2 3 | 4 5 6 | 7 8 9")
    print()

    kaka = string.ascii_uppercase

    for row_index, row in enumerate(data["puzzle"]):
        line = kaka[row_index] + "  "
        for col_index, val in enumerate(row):
            line += "_" if val is None else str(val)
            if col_index in (2, 5):
                line += " | "
            elif col_index != 8:
                line += " "
        print(line)
        if row_index in (2, 5):
            print("  ", "-" * 22)

display()
print("\n")
def display_solution():
    print("   1 2 3 | 4 5 6 | 7 8 9")
    print()

    kaka = string.ascii_uppercase

    for row_index, row in enumerate(data["solution"]):
        line = kaka[row_index] + "  "
        for col_index, val in enumerate(row):
            line += str(val)
            if col_index in (2, 5):
                line += " | "
            elif col_index != 8:
                line += " "
        print(line)
        if row_index in (2, 5):
            print("  ", "-" * 22)


while True:
    try:
        if data["puzzle"] == data["solution"]:
            print("Yayayayaaa U won the game")
            break

        c = input("\nEnter the place u want to fill number (example a5) or (give up):").upper()
        if c=="GIVE UP":
            print("\n-----------NOOB-----------")
            display_solution()
            break
        lala1 = ord(c[0]) - ord("A")
        lala2 = int(c[1]) - 1
        

            

        if data["puzzle"][lala1][lala2] is None:
            d = int(input("Enter number u want to place :"))

            if d == data["solution"][lala1][lala2]:
                data["puzzle"][lala1][lala2] = d
                print("\nCorrect!")
                display()
            else:
                print(f"\nWrong number — {d} doesn't belong in {c}. Try again.\n")

            

        else:
            print("\nThat place is already filled")
            continue

    except (IndexError, ValueError):
        print("yaya")

           