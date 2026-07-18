import requests
history=[]
while True:
  print("\n====== Country Information Explorer ======\n\n1. Search Country\n2. Compare Two Countries\n3. View Favourite Countries\n4. Show History\n5. Clear History\n6. Exit")
  poo=int(input("\nEnter choice according to your number (1 to 6) :"))
  if poo==1:
    country = input("Enter country name: ")

    url=f"https://api.api-ninjas.com/v1/country?name={country}"
    lala = {
            "X-Api-Key": "qRVMdtqb1nzwkOxTaMetnne4hUbd4fujCPhnsPf2"
        }

    a = requests.get(url, headers=lala)
    data=a.json()
    print(f"\t---------{country.upper()} Information---------\n")
    print("Fundamental Information\n")
    print("Name =",data[0]["name"])
    print("Capital =", data[0]["capital"])
    print("Region =",data[0]["region"])
    print("Currency name=",data[0]["currency"]["name"])
    print("\n")

    print("Economic information\n")
    print("GDP =",data[0]["gdp"])
    print("GDP per capita =",data[0]["gdp_per_capita"])
    print("GDP growth =", data[0]["gdp_growth"])
    print("Unemployment rate =",data[0]["unemployment"])
    print("\nDemographic Data\n")
    print("Population =",data[0]["population"])
    print("Sex ratio =",data[0]["sex_ratio"])
    print("Fertility =",data[0]["fertility"])
    print("Infant Mortality =",data[0]["infant_mortality"])
    history.append(f"Information of {country}")

  elif poo == 2:
      country1 = input("Enter the name of the first country to compare : ")
      country2 = input("Enter the name of the second country to compare : ")
      
      url1 = f"https://api.api-ninjas.com/v1/country?name={country1}" 
      url2 = f"https://api.api-ninjas.com/v1/country?name={country2}" 
      header = {
        "X-Api-Key": "qRVMdtqb1nzwkOxTaMetnne4hUbd4fujCPhnsPf2"
      }
      
      a1 = requests.get(url1, headers=header)
      data1 = a1.json()
      
      a2 = requests.get(url2, headers=header)
      data2 = a2.json()
      
      print(f"\t---------- {country1.upper()} vs {country2.upper()} ----------\n")
      
      print(f"{'GDP:':<22}{str(data1[0]['gdp']):<15} | {str(data2[0]['gdp']):<15}")
      print(f"{'Population:':<22}{str(data1[0]['population']):<15} | {str(data2[0]['population']):<15}")
      print(f"{'GDP Growth:':<22}{str(data1[0]['gdp_growth']):<15} | {str(data2[0]['gdp_growth']):<15}")
      print(f"{'GDP Per Capita:':<22}{str(data1[0]['gdp_per_capita']):<15} | {str(data2[0]['gdp_per_capita']):<15}")
      print(f"{'Unemployment Rate:':<22}{str(data1[0]['unemployment']):<15} | {str(data2[0]['unemployment']):<15}")
      print(f"{'Sex Ratio:':<22}{str(data1[0]['sex_ratio']):<15} | {str(data2[0]['sex_ratio']):<15}")
      history.append(f"Comparision of {country1} vs {country2}")

  elif poo==3:
    pass

  elif poo==4:
    if history:
      print("\n")
      print("-------History-------")
      for i,ele in enumerate(history,start=1) :
        print(f"{i}. {ele}")

    else:
      print("\nNo history found")
      
  
  elif poo==5:
    history.clear()

    
   



