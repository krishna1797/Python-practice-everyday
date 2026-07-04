#rock paper scissor game using python best of 5


import random
lala=("rock","paper", "scissor")

rounds=1
points=0
while True:
    yaya=random.choice(lala)
    print(f"\n==========ROUND{rounds}==========")
    a=input("\nEnter your selection ( rock , paper or scissor) :").lower()
    if(a==yaya):
        print("Computer choice =",yaya)
        print("Your Choice =",a)
        print("\nIts a DRAW 😐")
        rounds+=1
        print("your score =",points)
        
    elif(a=="rock"and yaya=="scissor") or (a=="paper" and yaya == "rock") or (a=="scissor"and yaya=="paper"):
        points+=1
        print("Computer choice =",yaya)
        print("Your Choice =",a)
        print("\nYou Won 🥳")
        print("your score =",points)
        
        rounds+=1
        
    elif(yaya=="rock"and a=="scissor") or (yaya=="paper" and a == "rock") or (yaya=="scissor"and a=="paper"):
        print("Computer choice =",yaya)
        print("Your Choice =",a)
        print("\nComputer Won 😭")
        rounds+=1
        print("your score =",points)
        
    else:
        print("Invalid choice")
        
    if(rounds==6):
        break
        
print(f"\nYour total score is {points} out of 5")
        