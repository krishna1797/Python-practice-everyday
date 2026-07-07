#movie ticket booking system using python




lala=[
    [" ","1","2","3","4","5","6"],
    ["A"," ","B","B"," "," "," "],
    ["B"," "," "," "," "," "," "],
    ["C"," "," "," "," "," "," "],
    ["D"," "," "," "," ","B","B"],
    ["E"," "," "," "," "," "," "],
    ["F"," "," "," "," ","B"," "],
    ]
        
print("Price of every seat is ₹250")
def theater ():
    for ele in lala:
        print(ele[0],"|",ele[1],"|",ele[2],"|",ele[3],"|",ele[4],"|",ele[5],"|",ele[6])
        print("---------------------------")
print("\n")
theater()

yaya=False
i=1

a=int(input("\nEnter number of seates u want to book :"))

while i<=a :
    yaya=False
    print(f"\nFor seat {i}")
    b=input("\nEnter row alphabet :").upper()
   
    for seat in lala :
        
        if seat[0]==b :
            c=int(input("Enter column number :"))
            if seat[c]==" ":
                seat[c]="B"
                theater()
                yaya=True
                i+=1
            else:
                print("\nSorry that seat is already booked")
                continue
            
            
    if not yaya:   
        print("\nINVALID CHOICE")
        continue
    
bill=250*a
while True:
    d=input("Do U want coke( yes or no) :").lower()
    if d=="yes":
        print("U will get ur drink in the middle of movie ")
        bill+=50
        break
        
        
    elif d=="no":
        print(" ")
        break
        
    else:
        print("Invalid choice ans in yes or no")
        
        
print("\nYour total bill is :",bill)