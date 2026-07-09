#Battleship game using python


print("This is a Battleship game. There are 10 ships on the board, but you only need to find 2 to win.")
import random
i=0
moves=0
score=0


board = [
    [" ", "1", "2", "3", "4", "5","6"],
    ["A", "~", "~", "~", "~", "~","~"],
    ["B", "~", "~", "~", "~", "~","~"],
    ["C", "~", "~", "~", "~", "~","~"],
    ["D", "~", "~", "~", "~", "~","~"],
    ["E", "~", "~", "~", "~", "~","~"],
    ["F", "~", "~", "~", "~", "~","~"]
]

playerboard = [
    [" ", "1", "2", "3", "4", "5", "6"],
    ["A", "~", "~", "~", "~", "~", "~"],
    ["B", "~", "~", "~", "~", "~", "~"],
    ["C", "~", "~", "~", "~", "~", "~"],
    ["D", "~", "~", "~", "~", "~", "~"],
    ["E", "~", "~", "~", "~", "~", "~"],
    ["F", "~", "~", "~", "~", "~", "~"]
]

def display ():
    for ele in playerboard:
        print(" ".join(ele))
    
display()
while i <10:
    a=random.randint(1,6)
    b=random.randint(1,6)
    if board[a][b] != "S":
        board[a][b]="S"
        i+=1

while True:
    
    try:
        c=input("Guess the location of battle ship (example a5) :").upper()
        lala1=ord(c[0])-ord("A")+1
        lala2=int(c[1])
      
        if board[lala1][lala2]=="~" :
            
            if playerboard[lala1][lala2]=="X":
                print("\nSorry that place was already filled")
                display()
                continue
            
            else:
                moves+=1
                print("\nMISS!!!!")
                print("No of tries =",moves)
                playerboard[lala1][lala2]="X"
                print("\n")
                display()
                
        
            
        elif board[lala1][lala2]=="S" :
            
            if playerboard[lala1][lala2]=="S" :
                print("\nSorry that place was already filled")
                display()
                continue
            else:
                moves+=1
                print("\nCongrats U just Found a Ship")
                print("No of tries =",moves)
                
                playerboard[lala1][lala2]="S"
                print("\n")
                display()
                score+=1
                
        else:
            print("Input invalid")
            
        if score==2 :
            print("\nU HAVE WON THE GAME!!!!!!!")
            print(f"u have won the game in just {moves} tries")
            display()
            print("\n")
            for el in board :
                print(" ".join(el))
            
    except :
        print("Invalid input")
        continue



    