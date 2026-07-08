import yaya
a=yaya.expenses
while True:
    try:
        print("\n1. Add Expense\n2. View Expenses date wise \n3. Total Spent\n4. Exit")
        food=0
        ent=0
        edu=0
        travel=0
        shop=0





        b=int(input("\nEnter number according to your work :"))

        if b==1 :
            c=input("\nEnter category :").title()
            d=int(input("Enter amount :"))
            e=input("Enter date :")

            a.append({"category" : c ,
                    "amount" : d,
                    "date" : e
                    })
        elif b==2 :
            print("---------Expenses---------")
            for i,ele in enumerate(a,start=1):
                print(i,"Categtory =",ele["category"])
                print(" Amount = ₹",ele["amount"])
                print(" Date =",ele["date"])
                print ("\n")



        elif b==3:
            for el in a:
                if el["category"]=="Food":
                    food+=el["amount"]

            for elee in a:
                if elee["category"]=="Education":
                    edu+=elee["amount"]

            for e in a:
                if e["category"]=="Travel":
                    travel+=e["amount"]
            for hmm in a:
                if hmm["category"]=="Entertainment":
                    ent+=hmm["amount"]
            for han in a:
                if han["category"]=="Shopping":
                    shop+=han["amount"]

            print("\n===========Total Expenses===========")
            print(f"FOOD = ₹{food}")
            print(f"SHOPPING = ₹{shop}")
            print(f"ENTERTAINMENT = ₹{ent}")
            print(f"EDUCATION = ₹{edu}")
            print(f"TRAVEL = ₹{travel}")
            print("-"*25)
            print(f"TOTAL = ₹{food+shop+ent+edu+travel}")

        elif b==4:
            print("Exit")
            break
    
    except:
        print("Enter a valid input")
        continue