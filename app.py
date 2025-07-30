import requests

api_key = '827486bdd99f0acec2c4482003666795'

city_name = input(" new delhi : ")

weather_data = requests.get(
    f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
)

if weather_data.status_code == 200:
    data = weather_data.json()
    weather = data['weather'][0]['main']
    temperature = data['main']['temp']
    print(f"Weather: {weather}, Temperature: {temperature}°C")
else:
    print("Error fetching weather data. Please check the city name and try again.")