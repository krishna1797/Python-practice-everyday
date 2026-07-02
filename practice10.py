print("welcome to KA resort😊 \nhere u will get rooms of your dreams".title())
print("We have all types of rooms from classic to delux")
print("\n1st floor is for classic rooms : ₹1200 per night\n2nd floor is for luxary rooms : ₹5000 per night\n3rd floor is for delux rooms : ₹9000 per night" )

dict={
    101:"avaliable",
    102:"avaliable",
    103:"booked",
    201:"avaliable",
    202:"booked",
    203:"avaliable",
    301:"avaliable",
    302:"booked",
    303:"booked"
}
while True:
    print("=============MENU=============")
    print("Enter (1) if U want to check room status")
    print("Enter (2) if U want to book a room")
    print("Enter (3) if U want to exit")
    
    a=int(input("\nEnter choice of your number :"))
    
    if (a==1):
        for ele in dict :
            print(ele,"status = ",dict[ele])
            
    elif(a==2):
        b=int(input("\nWhich room do U want :"))
        
        if(dict[b]=="booked"):
            print("\nWe are sorry that room is already booked😭")
        
        elif(dict[b]=="avaliable"):
            print("\nThat is really a great choice😃")
            c=int(input("How many nights do u want to stay :"))
            if b in (101,102,103):
                total=1200*c
                
            elif b in (201,202,203):
                total=5000*c
                
            elif b in (301,302,303):
                total=9000*c
                
            print("\nYour total for staying (",c,") nights is :",total)
            print("Hope u enjoyed your time in our hotel")
            print("Thanks for coming")
            break
        
    elif(a==3):
        print("\nThank you for visiting our hotel!")
        break
    else:
        print("invalid choice number".upper())
            