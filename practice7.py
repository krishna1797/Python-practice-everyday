#tic tac toe game made with function loop if else list logic this is two player game in my upcoming project u will see single player tic tac toe

lala=[
    ["","",""],
    ["","",""],
    ["","",""],
    ]
    
def display():
    print("\n")
    for ele in lala :
        print(" ",ele[0],"|",ele[1],"|",ele[2]," ")
        print("-----------")
        
def winner():
    #row
    for el in lala:
        if el[0]==el[1]==el[2]!="":
            return True
            
    #column        
    for i in range(3):
        if lala[0][i]==lala[1][i]==lala[2][i]!="":
            return True
            
    #column
    if lala[0][0]==lala[1][1]==lala[2][2]!="" or lala[2][0]==lala[1][1]==lala[0][2]!="":
        return True
        
    return False 

player="X"
moves=0

while True :
    
    display()
    
    print("\nPlayer",player)
    a=int(input("\nEnter row (0-2) :"))
    b=int(input("Enter column (0-2) :"))
        
    if (a>2 or a<0)or (b>2 or b<0):
        print("\nInvaild choice")
        continue
        
    elif (lala[a][b]!=""):
        print("\nThat box is already filled")
        continue
        
    else:
        lala[a][b]=player
        moves+=1
        
        
    if winner ():
        display()
        print(f"\nYayayaaaa Congratulationsss player {player} won the game")
        break
        
    if moves==9 :
        display()
        print("\nThe Match is Draw")
        break
        
    if (player=="X"):
        player ="O"
        
    else:
        player="X"
        
    