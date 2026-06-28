#this is a number guessing game using loop/break if elif and else it will also print your number or attempt

import random
no=random.randint(1,100)

print("Welcome to number game🥳🥳\nHere U have to guess a number between 1 to 100")
print("And u have to keep guessig until U guess the right number")
count=0
while True:
    A=int(input("\n Enter Your Number:"))
    if (A > no):
        print("Your guess is too high ☹️")
        count+=1
        print("Number of times u have tried:",count)
    elif (A<no):
        print("Your guess is too low 😞")
        count+=1
        print("Number of times u have tried:",count)
    else:
        print("Congratulations U got the corret number🎉💐💐🥳")
        count+=1
        print("U won the game in just (",count,") tries")
        break
