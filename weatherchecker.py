import requests
API_KEY = "6ac56b1b68a4f78da1ec97c8725b075a"

while True:
    city= input("Enter city name(or 'quit' to exit):")
    
    if city == "quit":
        break

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response=requests.get(url)
        data=response.json()

        if response.status_code == 200:
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            condition = data["weather"][0]["description"]
            wind_speed = data["wind"]["speed"]
            feels_like = data["main"]["feels_like"]
            
            print(f"City:{city}")
            print(f"Temprature:{temp}°C")
            print(f"Feels like:{feels_like}°C")
            print(f"Humidity:{humidity}%")
            print(f"Condition:{condition}")
            print(f"wind_speed:{wind_speed}km/h")
        else:
            print(f"Error: {data['message']}")

    except Exception as e :
        print(f"Error: {e}")            