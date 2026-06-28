#python code for calculator

print("---------Calculator---------")
a=float(input("\nEnter 1st number ="))
b=float(input("Enter 2nd number ="))
c=input("Enter the sign =")

if (c=="+"):
    print("Answer =",a+b)
    
elif(c=="-"):
    print("Answer =",a-b)
    
elif(c=="*"):
    print("Answer =",a*b)
    
elif(c=="/"):
    print("Answer =",a/b)

else:
    print("Invalid sign")