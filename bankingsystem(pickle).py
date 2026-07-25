import pickle


def save(lala):
    with open("yayafile", "ab") as f:
        pickle.dump(lala, f)

def read():
    try:
        with open("yayafile", "rb") as f:
            data = pickle.load(f)
            if not isinstance(data, list):
                return []
            return data
    except (FileNotFoundError, EOFError):
        return []
while True:
    print("========= BANK =========\n\n1. Create Account\n2. Login\n3. Exit")

    a = int(input("\nEnter number according to your work :"))
    if a == 1:
        accounts = read()

        name = input("\nEnter your full name :")

        while True:
            found = False
            id = input("Enter your unique ID :")
            for ele in accounts:
                if ele["ID"] == id:
                    found = True
            if found:
                print("This id is taken use different id")
                continue
            else:
                break

        phn = input("Enter your phn number :")
        email = input("Enter your email :")
        age = int(input("Enter your age :"))
        dep = int(input("Enter initial deposit :"))
        pas = input("Create password :")

        dict = {
            "ID": id,
            "Name of account holder": name,
            "phone number": phn,
            "E-mail": email,
            "Age": age,
            "Mony avaliable": dep,
            "Password": pas
        }

        accounts.append(dict)
        save(accounts)

        print("\nYour Account have been created")
        print("Name of account holder =", name, "ID =", id, "\nphone number =", phn, "\nE-mail =", email, "\nAge =", age, "\nMony avaliable =", dep)


    if a == 2:
        accounts = read()

        id = input("\nEnter your ID :")
        pas = input("Enter your password :")

        account = None
        for ele in accounts:
            if ele["ID"] == id and ele["Password"] == pas:
                account = ele

        if account is None:
            print("\nWrong ID or password")
        else:
            print("\nLogin successful")
            while True:
                print("1. Money deposit\n2. Money withdrawal\n3. Check balance\n4. Exit")
            
                b = int(input("\nEnter number according to your work :"))
            
                if b == 1:
                    amt = int(input("Enter amount to deposit :"))
                    account["Mony avaliable"] = account["Mony avaliable"] + amt
                    save(accounts)
                    print("\nDeposit successful. New balance =", account["Mony avaliable"])

                if b == 2:
                    amt = int(input("Enter amount to withdraw :"))
                    if amt > account["Mony avaliable"]:
                        print("\nInsufficient balance")
                    else:
                        account["Mony avaliable"] = account["Mony avaliable"] - amt
                        save(accounts)
                        print("\nWithdrawal successful. New balance =", account["Mony avaliable"])

                if b == 3:
                    print("\nYour balance =", account["Mony avaliable"])

                if b == 4:
                    print("\nThank you")
                    break


    if a == 3:
        print("\nThank you for visiting")
        break
