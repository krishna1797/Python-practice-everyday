import requests
import random
print("Welcome to KA quiz game")
print("1. Chose category and Difficulty of the quiz")
print("2. Play the quiz as it is")
LALA=True
yaya=True
score=0
umm=False
while True:
    try:

        haha=int(input("\nEnter number according to your choice :"))
        print("\n")
        if haha==1 :
            url="https://opentdb.com/api_category.php"
            a=requests.get(url)
            data=a.json()
            print("Difficulty = Easy , Medium or Hard\n")
            for ele in data["trivia_categories"]:
                print("Category id =",ele["id"],"\tCategory =",ele['name'])
            while yaya:
                yaya=False
                try:
                    idd=int(input("\nEnter Category id :"))
                    if idd>8 and idd<33:
                        
                        while LALA:
                            diff=input("Enter Diffculty :").lower()
                            if diff in ("easy","medium","hard"):
                                LALA=False
                                url1=f"https://opentdb.com/api.php?amount=10&category={idd}&difficulty={diff}&type=multiple"
                                u=requests.get(url1)
                                data1=u.json()
                                for l,poo in enumerate(data1["results"],start=1):
                                    print(f"{l}Q. {poo['question']}")
                                    option=poo["incorrect_answers"]
                                    option.append(poo["correct_answer"])
                                    random.shuffle(option)
                                    for m,pee in enumerate(option,start=1):
                                        print(f"{m}. {pee}")
                                    while True:
                                        
                                        try:
                                            hmm=int(input("\nEnter correct option number :"))
                                            if not(hmm>0 and hmm<5):
                                                print("Enter correct input")
                                                continue

                                            elif option[hmm-1]==poo["correct_answer"]:
                                                print("\nCORRECT ANSWER!!!!")
                                                score+=1
                                                umm=True
                                                print("\n")
                                                break
                                            elif option[hmm-1] in poo["incorrect_answers"]:
                                                print("\nIncorrect answer")
                                                print("Correct answer=",poo["correct_answer"])
                                                umm=True
                                                print("\n")
                                                break


                                        except:
                                            print("Enter integer only")
                                            continue

            
                            else:
                                print("Enter correct diffculty")
                                continue

                        

                    else:
                        print("\nEnter correct categoryy id")
                        continue
                except:
                    print("Enter integer value for category id ")
                    continue

            if umm:
                print(f"\nYOUR TOTAL SCORE = {score}")                   
                break
        
        



        
        elif haha == 2:
            url2="https://opentdb.com/api.php?amount=10&type=multiple"
            k=requests.get(url2)
            data2=k.json()
            for i,el in enumerate(data2["results"],start=1) :
                print(f"{i}Q. {el['question']}")
                options = el["incorrect_answers"]
                options.append(el["correct_answer"])
                random.shuffle(options)
                print("\n")
                for j,tata in enumerate(options,start=1) :
                    print(f"{j}. {tata}")
                while True:
                    try:
                        ans=int(input("\nEnter correct option number :"))
                        if not(ans>=1 and ans<=4):
                            print("Please enter option number")
                            continue


                        elif options[ans-1]==el["correct_answer"]:
                            print("\nCORRECT ANSWER!!!!")
                            score+=1
                            print("\n")
                            break
                        elif options[ans-1] in el["incorrect_answers"]:
                            print("\nIncorrect answer")
                            print("Correct answer=",el["correct_answer"])
                            print("\n")
                            break
                    except:
                        print("Enter integer valueeeee")

            print(f"\nYOUR TOTAL SCORE = {score}")  
            break

    except:
        print("Enter correct input")
        continue






