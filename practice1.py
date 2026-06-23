#This is a small beginner level menu program to practice if-else.


print("MENUU")
print(" 1. pizza - ₹250")
print(" 2. paneer - ₹1000")
print(" 3. pasta - ₹300")
print(" 4. roti - ₹10")

B=input("enter the dish u what to order:").lower()
C=int(input("enter quantity:"))

if(B=="pizza"):
    print("your total is =",250*C)
    
elif(B=="paneer"):
    print("your total is =",1000*C)
    
elif(B=="pasta"):
    print("your total is =",300*C)
    
elif(B=="roti"):
    print("your total is =",10*C)
    
else:
    print("chose from menu")