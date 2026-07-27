"""
BATTLESHIP
==========
A console-based Battleship game: You vs the Computer.

How to play:
- Each player has a 10x10 grid (columns A-J, rows 1-10).
- Ships are placed randomly at the start (yours are shown to you, the
  computer's are hidden until sunk).
- Take turns firing at coordinates (e.g. "B5") to try to sink all of the
  enemy's ships before they sink yours.
- 'X' = hit, 'O' = miss, ship letters = your own ships.

Run it with:
    python battleship.py
"""

import random

BOARD_SIZE = 10
COLS = "ABCDEFGHIJ"

SHIPS = [
    ("Carrier", 5),
    ("Battleship", 4),
    ("Cruiser", 3),
    ("Submarine", 3),
    ("Destroyer", 2),
]

EMPTY = "."
MISS = "O"
HIT = "X"


class Board:
    def __init__(self, name):
        self.name = name
        self.grid = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
       
        self.tracking = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]
        self.ships = {}  
        self.sunk = set()

    def place_ship_random(self, name, size):
        while True:
            horizontal = random.choice([True, False])
            if horizontal:
                r = random.randint(0, BOARD_SIZE - 1)
                c = random.randint(0, BOARD_SIZE - size)
                coords = [(r, c + i) for i in range(size)]
            else:
                r = random.randint(0, BOARD_SIZE - size)
                c = random.randint(0, BOARD_SIZE - 1)
                coords = [(r + i, c) for i in range(size)]

            if all(self.grid[rr][cc] == EMPTY for rr, cc in coords):
                for rr, cc in coords:
                    self.grid[rr][cc] = name[0]
                self.ships[name] = set(coords)
                return

    def place_all_ships(self):
        for name, size in SHIPS:
            self.place_ship_random(name, size)

    def receive_attack(self, r, c):
        """Returns ('hit'/'miss', ship_name_or_None, sunk_bool)"""
        for name, coords in self.ships.items():
            if (r, c) in coords:
                coords.discard((r, c))
                self.grid[r][c] = HIT
                sunk = len(coords) == 0
                if sunk:
                    self.sunk.add(name)
                return "hit", name, sunk
        self.grid[r][c] = MISS if self.grid[r][c] == EMPTY else self.grid[r][c]
        return "miss", None, False

    def all_ships_sunk(self):
        return len(self.sunk) == len(SHIPS)

    def print_board(self, reveal=True):
        header = "   " + " ".join(COLS)
        print(header)
        for r in range(BOARD_SIZE):
            row_cells = []
            for c in range(BOARD_SIZE):
                cell = self.grid[r][c]
                if not reveal and cell not in (HIT, MISS):
                    cell = EMPTY
                row_cells.append(cell)
            print(f"{r+1:>2} " + " ".join(row_cells))

    def print_tracking(self):
        header = "   " + " ".join(COLS)
        print(header)
        for r in range(BOARD_SIZE):
            print(f"{r+1:>2} " + " ".join(self.tracking[r]))


def parse_coordinate(s):
    s = s.strip().upper()
    if len(s) < 2:
        return None
    col_letter = s[0]
    row_part = s[1:]
    if col_letter not in COLS or not row_part.isdigit():
        return None
    row = int(row_part) - 1
    col = COLS.index(col_letter)
    if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
        return row, col
    return None


class ComputerAI:
    
    def __init__(self):
        self.tried = set()
        self.stack = []  
    def get_move(self):
        while self.stack:
            r, c = self.stack.pop()
            if (r, c) not in self.tried and 0 <= r < BOARD_SIZE and 0 <= c < BOARD_SIZE:
                self.tried.add((r, c))
                return r, c
        while True:
            r = random.randint(0, BOARD_SIZE - 1)
            c = random.randint(0, BOARD_SIZE - 1)
            if (r, c) not in self.tried:
                self.tried.add((r, c))
                return r, c

    def register_result(self, r, c, result):
        if result == "hit":
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if (nr, nc) not in self.tried:
                    self.stack.append((nr, nc))





def player_turn(player_board, computer_board):
    print("\n--- Your shots on the Computer ---")
    computer_board.print_tracking()
    while True:
        raw = input("\nEnter target coordinate (e.g. B5): ")
        coord = parse_coordinate(raw)
        if coord is None:
            print("Invalid input. Use a letter A-J followed by a number 1-10, e.g. C7.")
            continue
        r, c = coord
        if computer_board.tracking[r][c] != EMPTY:
            print("You already fired there. Try a different cell.")
            continue
        break

    result, ship_name, sunk = computer_board.receive_attack(r, c)
    computer_board.tracking[r][c] = HIT if result == "hit" else MISS

    if result == "hit":
        if sunk:
            print(f"HIT! You sunk the computer's {ship_name}!")
        else:
            print("HIT!")
    else:
        print("Miss.")

    return computer_board.all_ships_sunk()


def computer_turn(player_board, ai):
    r, c = ai.get_move()
    result, ship_name, sunk = player_board.receive_attack(r, c)
    ai.register_result(r, c, result)
    coord_str = f"{COLS[c]}{r+1}"
    print(f"\nComputer fires at {coord_str}...", end=" ")
    if result == "hit":
        if sunk:
            print(f"HIT! Your {ship_name} has been sunk!")
        else:
            print("HIT!")
    else:
        print("Miss.")
    return player_board.all_ships_sunk()


def main():
    
    print("Welcome to Battleship! Sink all 5 enemy ships before they sink yours.")
    print("Ships: " + ", ".join(f"{n} ({s})" for n, s in SHIPS))
    input("\nPress Enter to deploy your fleet...")

    player_board = Board("You")
    computer_board = Board("Computer")
    player_board.place_all_ships()
    computer_board.place_all_ships()

    ai = ComputerAI()

    print("\nYour fleet has been deployed:")
    player_board.print_board(reveal=True)

    turn = 1
    while True:
        print(f"\n===== Turn {turn} =====")

        computer_defeated = player_turn(player_board, computer_board)
        if computer_defeated:
            print("\n*** You win! All enemy ships have been sunk! ***")
            break

        player_defeated = computer_turn(player_board, ai)
        if player_defeated:
            print("\n*** The computer wins! All your ships have been sunk! ***")
            break

        print("\n--- Your fleet ---")
        player_board.print_board(reveal=True)

        turn += 1

    print("\nGame over. Thanks for playing!")


if __name__ == "__main__":
    main()