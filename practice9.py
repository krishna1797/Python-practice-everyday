#quiz game project in python 

print("Welcome to the quiz game here u have to enter correct answer of question given below ")


que={
    "1. What is the capital of india?" : "delhi",
    "2. Which Indian festival is known as the festival of lights?" : "diwali",
    "3. Which planet is known as the Red Planet?" : "mars",
    "4. How many days are there in a leap year?" : "366",
    "5. What is the hardest natural substance on Earth?" : "diamond",
    "6. Which is the largest continent in the world?" : "asia",
    "7. Which fruit is known as the king of fruits in India?" : "mango",
    "8. What is 90% of '50'??" : "45",
    "9. How many colors are there in a rainbow?" : "7",
    "10. Which is the national flower of india?" : "lotus"
    }
    
score=0
for yaya in que :
    print("\n",yaya)
    a=input("\nEnter your answer :").lower()
    if (a==que[yaya]):
        print("\n✅Correct!!!!🥳")
        score += 1
        
    else:
        print("\nYour entered answer (",a,") was wrong😭😭")
        print("correct answer was:",que[yaya])
        
print("="*50)
print("\nYour total score is '",score,"'out of 10")
percentage=(score/len(que))*100
print("Your total percentage is :",percentage)

        
        
    