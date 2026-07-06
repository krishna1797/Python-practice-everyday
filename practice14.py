#student management system using python


avg=0
i=1
def search ():
    b=int(input("\nEnter Roll no :"))
    for yaya in stu:
        if (b==yaya[1]):
            print("Student was found")
            print("\nName =",yaya[0])
            print("Roll No =",yaya[1])
            print("Marks =",yaya[2])
            return
    print(f"Sorry the student with roll no {b} was not found")
    
def update ():   
    c=int(input("Enter Roll no :"))
    d=int(input("Enter updated marks :"))
    for lala in stu:
        if (c==lala[1]):
            lala[2]=d
            print("\nName =",lala[0])
            print("Roll No =",lala[1])
            print("Updated Marks =",lala[2])
            return
    print(f"Sorry the student with roll no {c} was not found")
    
    
stu = [
    ["nakhil", 1061, 89],
    ["Rahul", 1062, 75],
    ["Aman", 1063, 91],
    ["Lala",1064,78],
    ["Yaya",1065,61],
    ["Yash",1066,64],
    ["Raghav",1067,77],
    ["natik",1068,54]
]


while True:
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    
    print("\n1. Show all students\n2. Add student\n3. Search student\n4. Update marks\n5. Find topper\n6. Average marks\n7. Exit")
    a=int(input("\nEnter your number :"))
    if (a==1):
        for ele in stu :
            print(f"\n-------Student{i}-------")
            print("Name :",ele[0])
            print("Roll No :",ele[1])
            print("Marks :",ele[2])
            i+=1
            
            
    elif(a==2):
        print("\nWrite the information of student u want to add")
        nam=input("\nStudent Name =")
        roll=int(input("Student Roll No ="))
        mar=int(input("Student Marks ="))
        stu.append([nam,roll,mar])
        
        
    elif(a==3):
        print("\nWrite the Roll No of student u want to search")
        search()
        
    elif(a==4):
        update()
        
    elif(a==5):
        topper = stu[0]   
        for student in stu:
            if student[2] > topper[2]:  
                topper = student          
        
        print("\n===== TOPPER =====")
        print("Name :", topper[0])
        print("Roll :", topper[1])
        print("Marks:", topper[2])
        
        
    elif (a==6):
        for stud in stu :
            avg+=stud[2]
        print("Average marks are :",avg/len(stu))
        
    elif (a==7):
        print("EXIT")
        break
    
    else:
        print("Enter correct input")