import requests 

api_key = '30d4741c779ba94c470ca1f63045390a'

user_input = input("Enter the city name: ")

weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("Invalid city")
else:
     temp = (weather_data.json()['main']['temp'])
     temp=(temp- 32) / 1.8
     t=round(temp)
     
     print(f"The temperature in {user_input} is: {t}ºC")
     print("The temperature in "+ user_input +" is :- " +str(t) + "ºC")


    