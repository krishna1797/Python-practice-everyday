#this is a updated ordering system u can have more than 1 dish here

print("MENUU")
print(" 1. pizza - ₹250")
print(" 2. paneer - ₹1000")
print(" 3. pasta - ₹300")
print(" 4. roti - ₹10")

bill=0

def yaya ():
    global bill

    B=input("enter the dish u what to order:").lower()
    C=int(input("enter quantity:"))

    if(B=="pizza"):
        total=250*C
        print("your total is:",total)
        bill+=total
    
    elif(B=="paneer"):
        total=1000*C
        print("your total is =",total)
        bill+=total
    
    elif(B=="pasta"):
        total=300*C
        print("your total is =",total)
        bill+=total
    
    elif(B=="roti"):
        total=10*C
        print("your total is =",total)
        bill=total+bill
    
    else:
        print("chose from menu")
        
    D=input("do u want any thing else (answer in yes or no):").lower()
    
    if (D=="yes"):
        yaya ()
    
    elif (D=="no"):
        print("your total bill is :",bill)
        print("thanks for ordering ,have a great day")
    
    else:
        print("answer in yes or no")
    
        
yaya ()


    
    
    
    
    
    
    
    
    
    
    
    
    