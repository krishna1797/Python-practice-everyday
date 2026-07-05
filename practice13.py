#library management using python

print("Welcome to KA library ")
lib= [
    "Hamlet", "William Shakespeare", 600,
    "Romeo and Juliet", "William Shakespeare", 800,
    "A Midsummer Night's Dream", "William Shakespeare", 500,
    "Harry Potter", "J.K. Rowling", 999,
    "The Casual Vacancy", "J.K. Rowling", 600,
    "The Silk Worm", "J.K. Rowling", 500,
    "Robinson Crusoe", "Daniel Defoe", 699,
    "Gulliver's Travels", "Jonathan Swift", 699,
    "To Kill a Mocking Bird", "Harper Lee", 700,
    "1984", "George Orwell", 499,
    "The lord of the rings", "J.R.R. Tolkien", 499,
    "The silent patient", "Alex Michaelides", 399,
    "The famous five", "Enid Blyton", 399,
    "The little prince", "Antoine de Saint-Exupéry", 599
]

while True:
    foundbuy=False
    foundsearch=False
    foundborrow=False
    print("\nEnter (1) if u want to see avaliable books")
    print("Enter (2) if u want to buy any book ")
    print("Enter (3) if u want to search any book")
    print("Enter (4) if u want to borrow any book")
    print("Enter (5) if u want to exit")
    
    a=int(input("\nEnter your number :"))
    if (a==1):
        print("\n==========Available Books==========")
        for i in range(0,len(lib),3):
            print("\n",lib[i],"written by",lib[1+i],"at = ₹",lib[2+i])
    
    elif(a==2):
        b=input("\nEnter the book u want to buy :").lower()
        for p in range(0,len(lib),3):
            if (lib[p].lower()==b):
                print("\nYour Total Buying Price is : ₹",lib[p+2])
                foundbuy=True
            
        if(foundbuy==False):
            print("\nSorry the booke was not found")

                
    elif(a==3):
        c=input("\nEnter the book u want to search :",).lower()
        for p in range(0,len(lib),3):
            if (lib[p].lower()==c):
                print("\nBook =",lib[p])
                print("\nAuthor =",lib[p+1])
                print("\nPrice = ₹",lib[p+2])
                foundsearch=True
                
        if(foundsearch==False):
            print("\nSorry the booke was not found")
            
                
    elif(a==4):
        print("Borrowing price for every book :",100)
        d=int(input("for how many days do u want to borrow the book :"))
        f=input("Enter book u want to borrow :").lower()
        for l in range(0,len(lib),3):
            if (lib[l].lower()==f):
                    print("\nYour Total Borrowing Price is : ₹",100*d)
                    foundborrow=True
            
        if(foundborrow==False):
             print("\nSorry the booke was not found")
            
                
    elif(a==5):
        print("Thanks for visiting our library")
        break
        
    else:
        print("put correct input")