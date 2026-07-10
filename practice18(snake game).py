import random
board=[]
snake=[
    [5,5],
    [5,4],
    [5,3],
    [5,2],
    [5,1]
    ]
lala=False

for i in range(10):
    row=[]
    board.append(row)
    for j in range(10):
        row.append(".")
        

def display():
    for row,col in snake:
        board[row][col]="S"
        
    board[snake[0][0]][snake[0][1]]="H"
    
    print("  1 2 3 4 5 6 7 8 9 10") 
    letter = "A" 
    for row in board: 
        print(letter, end=" ")
        for cell in row: 
            print(cell, end=" ") 
        print()
        letter = chr(ord(letter) + 1)
    
        
        
    
    
while True:
    if lala==True:
        print("U lost this Game 😔 ")
        break
        
        
    a=random.randint(0,9)
    b=random.randint(0,9)
    if board[a][b]==".":
        board[a][b]="@"
        
    else:
        continue
    
    display()
    print("\nUse (W)for moving up")
    print("Use (S)for moving down")
    print("Use (A)for moving left")
    print("Use (D)for moving right")
        
        
        
    while True:
        a=input("Move the snake using (W,A,S and D) :").upper()
        if a=="W":
            if board[snake[0][0]-1][snake[0][1]]==".":
                snake.insert(0,[snake[0][0]-1,snake[0][1]])
                tail_row,tail_col=snake.pop()
                board[tail_row][tail_col]="."
                display()
            
            elif board[snake[0][0]-1][snake[0][1]]=="@":
                snake.insert(0,[snake[0][0]-1,snake[0][1]])
                
                break
                
            else:
                print("YOUR SNAKE DIEDDD 😭")
                lala=True
                break
            
        elif a=="S":
            if board[snake[0][0]+1][snake[0][1]]==".":
                snake.insert(0,[snake[0][0]+1,snake[0][1]])
                tail_row,tail_col=snake.pop()
                board[tail_row][tail_col]="."
                display()
            
            elif board[snake[0][0]+1][snake[0][1]]=="@":
                snake.insert(0,[snake[0][0]+1,snake[0][1]])
                
                break
                
            else:
                print("\nYOUR SNAKE DIEDDD 😭")
                lala=True
                break
            
        elif a=="D":
            if board[snake[0][0]][snake[0][1]+1]==".":
                snake.insert(0,[snake[0][0],snake[0][1]+1])
                tail_row,tail_col=snake.pop()
                board[tail_row][tail_col]="."
                display()
            
            elif board[snake[0][0]][snake[0][1]+1]=="@":
                snake.insert(0,[snake[0][0],snake[0][1]+1])
                break
                
            else:
                print("\nYOUR SNAKE DIEDDD 😭")
                lala=True
                break
                
        elif a=="A":
            if board[snake[0][0]][snake[0][1]-1]==".":
                snake.insert(0,[snake[0][0],snake[0][1]-1])
                tail_row,tail_col=snake.pop()
                board[tail_row][tail_col]="."
                display()
            
            elif board[snake[0][0]][snake[0][1]-1]=="@":
                snake.insert(0,[snake[0][0],snake[0][1]-1])
                
                break
                
            else:
                print("\nYOUR SNAKE DIEDDD 😭")
                lala=True
                break
    
        else:
            print("Invalid input please enter correct input")
    