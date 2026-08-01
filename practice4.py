#this is a updated ordering system u can have more than 1 dish here

menu = {
    "pizza": 250,
    "paneer": 1000,
    "pasta": 300,
    "roti": 10
}
 
GST_RATE = 0.05  
 
bill = 0
order_history = []  
 
 
def display_menu():
    print("MENUU")
    for item, price in menu.items():
        print(f" {item.title()} - ₹{price}")
 
 
def yaya():
   
    global bill
 
    B = input("enter the dish u what to order:").lower().strip()
 
    
    if B not in menu:
        print("chose from menu")
    else:
       
        try:
            C = int(input("enter quantity:"))
            if C <= 0:
                print("quantity must be a positive number")
            else:
                total = menu[B] * C
                print("your total is:", total)
                bill += total
                order_history.append((B, C, total))  
        except ValueError:
            print("please enter a valid number for quantity")
 
    while True:
        D = input("do u want any thing else (answer in yes or no):").lower().strip()
        if D == "yes":
            return True
        elif D == "no":
            return False
        else:
            print("answer in yes or no")
 
 
def print_receipt():
   
    print("\n----- RECEIPT -----")
    for B, C, total in order_history:
        print(f" {B.title()} x{C} = ₹{total}")
 
    tax = round(bill * GST_RATE, 2)
    grand_total = round(bill + tax, 2)
 
    print("--------------------")
    print("subtotal:", bill)
    print(f"GST ({int(GST_RATE * 100)}%):", tax)
    print("grand total:", grand_total)
    print("thanks for ordering ,have a great day")
 
 

display_menu()
want_more = True
while want_more:
    want_more = yaya()
 
print_receipt()
 
    
    
    
    
    
    
    
    
    
    
    
