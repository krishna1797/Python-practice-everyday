print("WELCOME TO KA media")
print("__________Main menu___________")
social = [
    {
        "username": "krishna_12",
        "password": "abc12345",
        "followers": 100,
        "following": 150,
        "posts": [
            {
                "caption": "Hello everyone!",
                "likes": ["lala_8", "soham_sharma1"]
            },
            {
                "caption": "Learning Python today.",
                "likes": ["shaurya_2009"]
            }
        ]
    },
    {
        "username": "lala_8",
        "password": "lala1234",
        "followers": 300,
        "following": 250,
        "posts": [
            {
                "caption": "Beautiful sunset 🌅",
                "likes": ["krishna_12"]
            }
        ]
    },
    {
        "username": "soham_sharma1",
        "password": "password123",
        "followers": 100,
        "following": 150,
        "posts": [
            {
                "caption": "First day at college!!!",
                "likes": []
            }
        ]
    },
    {
        "username": "shaurya_2009",
        "password": "2009shaurya",
        "followers": 100,
        "following": 150,
        "posts": [
            {
                "caption": "Playing football today ⚽",
                "likes": ["krishna_12", "lala_8"]
            }
        ]
    }
]
print("\n1. Signup\n2. Login\n3. Exit\n")

while True:
    try:
        a = int(input("Enter number according to your work: "))

        if a in [1, 2, 3]:
            if a==1:
                print("-----------Sign Up Page-----------\n")
                while True:
                    user=input("Enter username =")
                    found = False
                    for ele in social :
                        if ele["username"]==user:
                            print("\nSorry username already exist\n")
                            found = True
                            break
                    if not found  :
                        print("Username accepted:", user)
                        break

                while True:

                    pas=input("\nCreate password =")
                    if len(pas)<8 :
                        print("Length of password should be more than 8 character\n")
                        continue
                
                    else:
                        break




                while True :

                    cpass=input("Conform password =")
                    if pas!=cpass :
                        print("\npassword should be equal to conform password\n")
                        continue
                    else:
                        break
                profile={
                    "username": user,
                    "password":pas,
                    "followers":0,
                    "following":0,
                    "posts":[
                        {"caption" : "Hello, just joined KA media",
                        "likes" : []
                        }
                    ]
                }
                print("\nYayayaa your profile is created\n")
                print("----------Your profile----------")
                print("username =", user)
                print("password =", pas)
                print("followers =", 0)
                print("following =", 0)
                social.append(profile)
                while True:
                    print("\n\nA = See others post")
                    print("B = Add a post")
                    print ("C = Logout")
    
                    yaya=input("Chose a alphabet according to your work :").upper()
                    print("\n\n")
                    if yaya=="A":
                        i=1
                        postslist=[]
                        for ele in social:    
                            for el in ele["posts"]:
                                
                                print(f"{i}. User = {ele['username']}")
                                print("   post =",el["caption"])
                                print("   Likes =",len(el["likes"]))
                                postslist.append(el)
                                i+=1
                                print("\n")
                            print("\n")
                        while True :
                            try:
                                likepost=int(input("Enter the post u want to like :"))
                                selectedpost=postslist[likepost-1]
                                if user not in selectedpost["likes"]:
                                    selectedpost["likes"].append(user)
                                    print("\n")
                                    print(selectedpost["caption"])
                                    print(len(selectedpost["likes"]),"Likes")
                                    print("\n")
                                    wwe=input("Do u want to like any other post (yes/no) :")
                                    if wwe=="yes":
                                        continue
                                            
                                    elif wwe=="no":
                                        break
                                    else:
                                        print("please answer in yes or no")
                                        continue
                                else:
                                    print("\nU have already liked this post")
                                    continue
                                
                                

                            except:
                                print("Enter correct integer") 
                                continue
                    elif yaya == "B":
                        caption = input("Enter your post caption :")

                        for ele in social:
                            if ele["username"] == user:
                                ele["posts"].append({
                                    "caption": caption,
                                    "likes": []
                                })

                                print("\n✅ Post uploaded successfully!\n")
                                print("Your Posts:\n")

                                i = 1
                                for post in ele["posts"]:
                                    print(f"{i}. {post['caption']}")
                                    print(f"   Likes: {len(post['likes'])}\n")
                                    i += 1
                                break
                    elif yaya=="C":
                        break
            elif a==2:

                while True:
                    login_profile=[]
                    login=False
                    existing=input("Enter your existing user name :")
                    for pee in social:
                        if pee["username"] == existing :
                            password=input("Enter password :")
                            if pee["password"]==password:
                                print("Login Successfully")
                                login_profile.append(pee)
                                login=True
                        
                    if login:
                        print("\nID login Successful\n")
                        print("-------Your profile-------")
                        for i in login_profile:
                            print("Username =",i["username"])
                            print("password =",i["password"])
                            print("Followers =",i["followers"])
                            print("Following =",i["following"])
                        while True:
                            print("\nA= View your post")
                            print("B= Add any post")
                            print("C= View everyones post")
                            print("D= Exit")
                            alpa=input("Enter alphabet according to your work :").upper()
                            if alpa=="A":
                                print("\n")
                                for i in login_profile:
                                    for j,k in enumerate(i["posts"],start=1):
                                        print(j,". ",k["caption"])
                                        print("   Likes",len(k["likes"]))
                            elif alpa == "B":
                                add=input("Enter caption of new post :")
                                login_profile[0]["posts"].append({"caption" : add , "likes" : []})
                                print("\nYour post added")

                            elif alpa == "C":
                                
                                i = 1
                                postslist = []

                                for ele in social:
                                    if ele["username"] != login_profile[0]["username"]:

                                        for post in ele["posts"]:
                                            print(f"{i}. User = {ele['username']}")
                                            print(f"   Post = {post['caption']}")
                                            print(f"   Likes = {len(post['likes'])}")
                                            print()

                                            postslist.append(post)
                                            i += 1

                                while True:
                                    try:
                                        likepost = int(input("Enter the post number you want to like: "))

                                        if 1 <= likepost <= len(postslist):
                                            selectedpost = postslist[likepost - 1]

                                            if login_profile[0]["username"] not in selectedpost["likes"]:
                                                selectedpost["likes"].append(login_profile[0]["username"])
                                                print("Post liked successfully!")
                                                print("Likes:", len(selectedpost["likes"]))
                                            else:
                                                print("You have already liked this post.")
                                        else:
                                            print("Invalid post number.")

                                        choice = input("Like another post? (yes/no): ").lower()

                                        if choice == "no":
                                            break

                                    except ValueError:
                                        print("Please enter a valid number.")
                            elif alpa=="D":
                                break
        
                                



                    else:
                        print("Login unsuccessfull")

            elif a==3:
                print("\nThanks for visiting")
                break

                                
                            
                                
                                
                                
                                
                                



                            

        else:
            print("Please enter 1, 2, or 3.")

    except:
        print("Please enter a valid number.")
        continue
