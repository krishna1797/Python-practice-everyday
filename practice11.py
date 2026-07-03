#ATM transection machine using python

balance=10000

print("======== ATM ========")

while True:
    print("\nChose the number according to your work")
    print("1. Check balance")
    print("2. Money deposit")
    print("3. Money withdrawal")
    print("4. EXIT")
    
    a=int(input("\nEnter a number according to your work :"))
    if(a==1):
        print("\nYour current balance is : ₹",balance)
        
    elif(a==2):
        b=int(input("\nEnter the amount u want to deposit :"))
        print(f"Amount of ₹{b} have been deposited")
        balance+=b
        print(f"\nTotal balance in your account is :₹{balance}")
        
        
    elif(a==3):
        c=int(input("\nEnter amount u want to withdraw :"))
        if ((balance-c)>=0):
            print(f"Amount of{c}have been deducted from your account")
            balance-=c
            print(f"\nTota balance in your account is :₹{balance}")
            
        else:
            print(f"Sorry the transection was cancelled because u have ₹{balance}")
            
    elif(a==4):
        print("\nthank u for using your transection system".title())
        break
    
    else:
        
        print("\nenter a correct number between 1 to 4 according to your work ".upper())
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        