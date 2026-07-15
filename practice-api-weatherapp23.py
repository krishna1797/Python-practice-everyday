import requests
print("============KA Weather info============")

city=input("\nEnter city name to get information :")
limit=1
APIkey="750867515d6d6561f40dbd7da7485ff0"
url=f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit={limit}&appid={APIkey}"
lala=requests.get(url)
data=lala.json()
a=(data[0]["lat"])
b=(data[0]["lon"])
API="f7e41ce7e70845cc2b06568cfc7cfb4c"
url2=f"https://api.openweathermap.org/data/2.5/weather?lat={a}&lon={b}&appid={API}&units=metric"
lala2=requests.get(url2)
data2=lala2.json()

print("\n-------------infromation--------------")
print(f"\nType of Weather in {city} : {data2['weather'][0]['main']}")
print(f"Current Temperture : {data2["main"]["temp"]}°C")
print(f"Highest temperature : {data2["main"]["temp_max"]}°C")
print(f"Lowest temperature : {data2["main"]["temp_min"]}°C")
print(f"Humidity in {city} : {data2["main"]["humidity"]}%")
print(f"Wind Speed : {data2["wind"]["speed"]} m/s.")

