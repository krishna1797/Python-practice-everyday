import pickle
import os

DATA_FILE = "expenses.pkl"

DEFAULT_EXPENSES = [
    {"category": "Entertainment", "amount": 200, "date": "03-06-2026"},
    {"category": "Shopping", "amount": 1000, "date": "04-06-2026"},
    {"category": "Education", "amount": 400, "date": "06-06-2026"},
    {"category": "Food", "amount": 250, "date": "08-06-2026"},
    {"category": "Travel", "amount": 200, "date": "10-06-2026"},
    {"category": "Food", "amount": 300, "date": "13-06-2026"},
    {"category": "Entertainment", "amount": 100, "date": "16-06-2026"},
    {"category": "Travel", "amount": 500, "date": "20-06-2026"},
    {"category": "Shopping", "amount": 350, "date": "21-06-2026"},
    {"category": "Food", "amount": 100, "date": "25-06-2026"},
    {"category": "Education", "amount": 160, "date": "28-06-2026"},
]


def load_expenses():
    """Load saved expenses from disk. If there's no saved file yet,
    or the saved file is empty, start with the default expenses list."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "rb") as f:
                data = pickle.load(f)
            if data:
                return data
        except (pickle.UnpicklingError, EOFError):
            print("Saved data was corrupted, starting fresh.")
    return list(DEFAULT_EXPENSES)


def save_expenses(expenses):
    """Save the current expenses list to disk."""
    with open(DATA_FILE, "wb") as f:
        pickle.dump(expenses, f)


def add_expense(expenses):
    c = input("\nEnter category :").title()
    while True:
        try:
            d = int(input("Enter amount :"))
            break
        except ValueError:
            print("Amount must be a number, try again.")
    e = input("Enter date :")
    expenses.append({"category": c, "amount": d, "date": e})
    save_expenses(expenses)
    print("Expense added and saved.")


def view_expenses(expenses):
    print("---------Expenses---------")
    if not expenses:
        print("No expenses recorded yet.")
        return
    for i, ele in enumerate(expenses, start=1):
        print(i, "Category =", ele["category"])
        print(" Amount = ₹", ele["amount"])
        print(" Date =", ele["date"])
        print()


def total_spent(expenses):
    totals = {}
    for ele in expenses:
        cat = ele["category"]
        totals[cat] = totals.get(cat, 0) + ele["amount"]

    print("\n===========Total Expenses===========")
    for category, amount in totals.items():
        print(f"{category.upper()} = ₹{amount}")
    print("-" * 25)
    print(f"TOTAL = ₹{sum(totals.values())}")


def main():
    expenses = load_expenses()

    while True:
        try:
            print("\n1. Add Expense\n2. View Expenses date wise \n3. Total Spent\n4. Exit")
            choice = int(input("\nEnter number according to your work :"))

            if choice == 1:
                add_expense(expenses)
            elif choice == 2:
                view_expenses(expenses)
            elif choice == 3:
                total_spent(expenses)
            elif choice == 4:
                save_expenses(expenses)
                print("Saved. Exit")
                break
            else:
                print("Enter a valid input")

        except ValueError:
            print("Enter a valid input")
            continue


if __name__ == "__main__":
    main()
