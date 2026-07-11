import random
print("========Hangman========\n")

lives=7



list=[]
def hangman (pee):
    global lives
    lala=random.choice(pee)
    for ele in lala:
        list.append("_")
    print("Word",end=" = ")

    
    for ele in list :
        print(ele,end=" ")
    while True:
        if lives==0:
            print("\nU lost the game 😔\n")
            print("Word =",lala)
            break
        if "_" not in list :
            print("\n\nYOU WONN🥳\n")
            break
            
            
        guess = input("\n\nEnter a letter :").lower()
    
        if guess in lala:
            for i in range(len(lala)):
                if lala[i] == guess:
                    list[i] = guess
            for ele in list:
                print(ele,end=" ")
    
        else:
            print("\nThis letter is not present!😓")
            lives-=1
            print("U lost 1 life")
            print("lives left =",lives)
        
    
    
    
print("1. Animals\n2. Fruits\n3. Country\n4. Random" )
animals = [
    "lion", "tiger", "elephant", "rabbit", "octopus", "penguin",
    "shark", "sheep", "horse", "pig", "dragonfly", "butterfly",
    "owl", "lobster", "crocodile", "peacock", "donkey",
    "caterpillar", "hippopotamus","turtle","pigeon",'Whale'
]
fruits = ["apple", "banana", "mango", "orange", "kiwi",
         "coconut", "lemon","grape", "pineapple","watermelon",
         "papaya","gooseberry","guava", "lychee","peach", "pear", "plum",
         "apricot", "nectarine", "pomegranate", "strawberry", "blueberry",
         ]

countries = [
    "india", "japan", "canada", "brazil", "belgium", "afghanistan",
    "denmark", "indonesia", "iran", "iraq", "ireland", "israel",
    "italy", "thailand", "bhutan", "philippines", "portugal",
    "kazakhstan", "france", "mexico", "russia", "malaysia","sweden"
]
a=int(input("\nEnter number according to your choice :"))
if a==1 :
   hangman(animals)
   
   
elif a==2:
    hangman(fruits)
    
elif a==3:
    hangman(countries)
    
elif a==4:
    yaya=random.choice([animals,fruits,countries])
    hangman(yaya)
