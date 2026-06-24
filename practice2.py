'''
This is a project to practice loop with if/elif/else 
In this u can buy your desired items form tha available items
'''
A={
    "bread":40,
    "pizza base":400,
    "egg":4,
    "pen":44,
    "copy":10
}
bill=0
print("welcome to yaya mart")
print("every thing u are wishing for is avaliable here")

while True:
    print("avalable items are:-")
    for ele in A:
        print(ele,"=₹",A[ele])
        
    B=input("enter the item u want to buy(or type 'done') :").lower()
    
    
    if B in A:
        Q=int(input("enter quantity:"))
        total=A[B]*Q
        print("your total is = ₹",total)
        bill=total+bill
        
    elif (B=="done"):
        break
    
    else:
        print("item is not avalable")
        
print("your total bill is:",bill)
print("thanks for shopping")