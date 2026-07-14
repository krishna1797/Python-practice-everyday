import requests
i=1


key="da0dcf1e2a374becc869b134f1aee63b"



print("Enter (1) to get recent news headlines")
print("Enter (2) to search news")

try:
    no=int(input("Enter number :"))





    if no==1:
        print("=========Head Lines=========")
        url=f"https://gnews.io/api/v4/top-headlines?country=in&lang=en&apikey={key}"
        a=requests.get(url)
        data=a.json()

        for ele in data["articles"]:
            print(f"{i}. {ele["title"]}")
            i+=1

    elif no==2:
        lala=input("Enter topic or person :")
        print(f"---------News about {lala}---------")
        searchurl=f"https://gnews.io/api/v4/search?q={lala}&lang=en&apikey={key}" 
        b=requests.get(searchurl)
        data2=b.json()
        if data2["totalArticles"] == 0:
            print("No news found.")
        else:
            for j, article in enumerate(data2["articles"], start=1):
                print(f"{j}. {article['title']}")


except:
    print("Please enter a correct integerand retry")










