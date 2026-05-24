import requests

API_KEY = "ebae1bb7f3fab53a5c5886a0e6e9cf6f"

city = input("Enter city name: ")

# Get Latitude & Longitude
geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid=ebae1bb7f3fab53a5c5886a0e6e9cf6f"

geo_response = requests.get(geo_url)
geo_data = geo_response.json()

lat = geo_data[0]["lat"]
lon = geo_data[0]["lon"]

print("Latitude:", lat)
print("Longitude:", lon)

# Solar API
solar_url = f"https://api.openweathermap.org/energy/2.0/solar/panels?lat={lat}&lon={lon}&appid=ebae1bb7f3fab53a5c5886a0e6e9cf6f"

solar_response = requests.get(solar_url)

print("\nSolar API Status Code:", solar_response.status_code)
print("Solar Data Fetched Successfully")

# -------OUTPUT--------
# Enter city name: jaipur
# Latitude: 26.9154576
# Longitude: 75.8189817

# Solar API Status Code: 401
# Solar Data Fetched Successfully