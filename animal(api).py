import requests
history=[]
while True:
  print("\n====== Animal Encyclopedia ======\n\n1. Search Animal\n2. Compare Two Animals\n3. Show History\n4. Clear History\n5. Exit")
  poo=int(input("\nEnter choice according to your number (1 to 5) :"))
  try:
    if poo==1:
      animal = input("Enter animal name: ")

      url=f"https://api.api-ninjas.com/v1/animals?name={animal}"
      lala = {
              "X-Api-Key": "qRVMdtqb1nzwkOxTaMetnne4hUbd4fujCPhnsPf2"
          }

      a = requests.get(url, headers=lala)
      data=a.json()
      print(f"\t---------{animal.upper()} Information---------\n")
      print("Fundamental Information\n")
      print("Name =",data[0]["name"])
      print("Scientific name =", data[0]["taxonomy"]["scientific_name"])
      print("Family =",data[0]["taxonomy"]["family"])
      print("Locations =",data[0]["locations"])
      print("\n")

      print("Characteristics\n")
      print("Diet =",data[0]["characteristics"].get("diet"))
      print("Habitat =",data[0]["characteristics"].get("habitat"))
      print("Lifespan =", data[0]["characteristics"].get("lifespan"))
      print("Top speed =",data[0]["characteristics"].get("top_speed"))
      print("\nMore Details\n")
      print("Weight =",data[0]["characteristics"].get("weight"))
      print("Length =",data[0]["characteristics"].get("length"))
      print("Group behavior =",data[0]["characteristics"].get("group_behavior"))
      print("Predators =",data[0]["characteristics"].get("predators"))
      history.append(f"Information of {animal}")

    elif poo == 2:
        animal1 = input("Enter the name of the first animal to compare : ")
        animal2 = input("Enter the name of the second animal to compare : ")

        url1 = f"https://api.api-ninjas.com/v1/animals?name={animal1}"
        url2 = f"https://api.api-ninjas.com/v1/animals?name={animal2}"
        header = {
          "X-Api-Key": "qRVMdtqb1nzwkOxTaMetnne4hUbd4fujCPhnsPf2"
        }

        a1 = requests.get(url1, headers=header)
        data1 = a1.json()

        a2 = requests.get(url2, headers=header)
        data2 = a2.json()

        print(f"\t---------- {animal1.upper()} vs {animal2.upper()} ----------\n")

        print(f"{'Diet:':<22}{str(data1[0]['characteristics'].get('diet')):<15} | {str(data2[0]['characteristics'].get('diet')):<15}")
        print(f"{'Habitat:':<22}{str(data1[0]['characteristics'].get('habitat')):<15} | {str(data2[0]['characteristics'].get('habitat')):<15}")
        print(f"{'Lifespan:':<22}{str(data1[0]['characteristics'].get('lifespan')):<15} | {str(data2[0]['characteristics'].get('lifespan')):<15}")
        print(f"{'Top speed:':<22}{str(data1[0]['characteristics'].get('top_speed')):<15} | {str(data2[0]['characteristics'].get('top_speed')):<15}")
        print(f"{'Weight:':<22}{str(data1[0]['characteristics'].get('weight')):<15} | {str(data2[0]['characteristics'].get('weight')):<15}")
        print(f"{'Length:':<22}{str(data1[0]['characteristics'].get('length')):<15} | {str(data2[0]['characteristics'].get('length')):<15}")
        history.append(f"Comparision of {animal1} vs {animal2}")


    elif poo==3:
      if history:
        print("\n")
        print("-------History-------")
        for i,ele in enumerate(history,start=1) :
          print(f"{i}. {ele}")

      else:
        print("\nNo history found")


    elif poo==4:
      history.clear()
      print("History is cleared")

    elif poo==5:

      break

  except:
    print("\nEnter interger only")