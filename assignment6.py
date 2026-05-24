import requests
from datetime import datetime

# Your API Key
API_KEY = "YOUR_API_KEY"

# City Name
city = input("Enter city name: ")

# API URL
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=8a4aba68ec7cfb91c28425328c3912b5"

# Request to API
response = requests.get(url)

# Convert response to JSON
data = response.json()

# Check city found or not
if data["cod"] != 200:
    print("City not found!")
else:
    # Fetch data
    city_name = data["name"]
    country = data["sys"]["country"]

    temp = data["main"]["temp"]
    feels_like = data["main"]["feels_like"]
    humidity = data["main"]["humidity"]
    pressure = data["main"]["pressure"]

    weather = data["weather"][0]["description"]

    wind_speed = data["wind"]["speed"]

    visibility = data["visibility"]

    sunrise = datetime.fromtimestamp(data["sys"]["sunrise"])
    sunset = datetime.fromtimestamp(data["sys"]["sunset"])

    # Display data
    print("\n------ Weather Report ------")
    print(f"City        : {city_name}, {country}")
    print(f"Temperature : {temp} °C")
    print(f"Feels Like  : {feels_like} °C")
    print(f"Condition   : {weather}")
    print(f"Humidity    : {humidity}%")
    print(f"Pressure    : {pressure} hPa")
    print(f"Wind Speed  : {wind_speed} m/s")
    print(f"Visibility  : {visibility} meters")
    print(f"Sunrise     : {sunrise}")
    print(f"Sunset      : {sunset}")

# -------OUTPUT--------
# Enter city name: jaipur

# ------ Weather Report ------
# City        : Jaipur, IN
# Temperature : 309.77 °C
# Feels Like  : 307.92 °C
# Condition   : haze
# Humidity    : 19%
# Pressure    : 1003 hPa
# Wind Speed  : 5.66 m/s
# Visibility  : 3500 meters
# Sunrise     : 2026-05-24 05:35:21
# Sunset      : 2026-05-24 19:12:02
   