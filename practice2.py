'''
This is a project to practice loop with if/elif/else 
In this u can buy your desired items form tha available items
'''
A = {
    "bread": 40,
    "pizza base": 400,
    "egg": 4,
    "pen": 44,
    "copy": 10
}

stock = {
    "bread": 50,
    "pizza base": 20,
    "egg": 100,
    "pen": 200,
    "copy": 150
}

bill = 0
receipt = []

print("=" * 50)
print("WELCOME TO YAYA MART".center(50))
print("Everything you are wishing for is available here!".center(50))
print("=" * 50)

while True:
    print("\nAvailable items are:-")
    print("-" * 40)
    print(f"{'Item':<15}{'Price(₹)':<12}{'Stock':<10}")
    print("-" * 40)
    for ele in A:
        print(f"{ele:<15}{A[ele]:<12}{stock[ele]:<10}")
    print("-" * 40)

    B = input("Enter the item you want to buy (or type 'done'): ").lower().strip()

    if B in A:
        try:
            Q = int(input("Enter quantity: "))
            if Q <= 0:
                print("Quantity must be a positive number!")
                continue
            if Q > stock[B]:
                print(f"Sorry, only {stock[B]} unit(s) of {B} left in stock!")
                continue
        except ValueError:
            print("Invalid quantity! Please enter a whole number.")
            continue

        total = A[B] * Q
        stock[B] -= Q
        bill += total
        receipt.append((B, Q, A[B], total))
        print(f"{Q} x {B} added to cart. Subtotal: ₹{total}")

    elif B == "done":
        if not receipt:
            print("You didn't buy anything. Visit again!")
        break

    else:
        print("Item is not available.")

if receipt:
    print("\n" + "=" * 50)
    print("YOUR BILL / RECEIPT".center(50))
    print("=" * 50)
    print(f"{'Item':<15}{'Qty':<6}{'Price':<10}{'Total':<10}")
    print("-" * 50)
    for item, qty, price, subtotal in receipt:
        print(f"{item:<15}{qty:<6}{price:<10}{subtotal:<10}")
    print("-" * 50)

    discount = 0
    if bill > 500:
        discount = bill * 0.10
        print(f"Congrats! You get a 10% discount: -₹{discount:.2f}")
    final_bill = bill - discount

    print(f"\nSubtotal: ₹{bill}")
    if discount:
        print(f"Discount: ₹{discount:.2f}")
    print(f"Final Bill: ₹{final_bill:.2f}")
    print("=" * 50)

print("\nThanks for shopping at Yaya Mart! Visit again ")

print("thanks for shopping")
