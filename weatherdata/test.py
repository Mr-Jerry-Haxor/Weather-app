'''
import requests

def get_location(zipcode):
    url = f"https://api.postalpincode.in/pincode/{zipcode}"
    response = requests.get(url)
    data = response.json()
    if data[0]['Status'] == 'Success':
        location = data[0]['PostOffice'][0]['Name']
        state = data[0]['PostOffice'][0]['State']
        district = data[0]['PostOffice'][0]['District']
        return f"{location}, {district}, {state}"
    else:
        return "Invalid ZIP code."

zipcode = input("Enter ZIP code: ")
print(get_location(zipcode))


import requests

# OpenWeatherMap API endpoint URL
url = "http://api.openweathermap.org/data/2.5/weather"

# Your API key from OpenWeatherMap
api_key = "fd57d36cb6c5170defff8b9abbe5f32d"

# Location you want to get the weather for (using city name)
location = "Nalgonda"

# Build the API endpoint URL
endpoint = f"{url}?q={location}&appid={api_key}&units=metric"

# Send an HTTP request to the API and get the response
response = requests.get(endpoint)

# Parse the JSON response
weather_data = response.json()

# Extract the temperature and description from the response
# temperature = weather_data["main"]["temp"]
# description = weather_data["weather"][0]["description"]

# Print the temperature and description
# print(f"The temperature in {location} is {weather_data} degrees Celsius and the weather is {weather_data}.")
print(weather_data)
'''

from geopy.geocoders import Nominatim

# initialize Nominatim geocoder
geolocator = Nominatim(user_agent="my_app")

# define the latitude and longitude
latitude = 17.0622976
longitude = 79.2625152

# perform reverse geocoding
location = geolocator.reverse(f"{latitude}, {longitude}")

# print the address
print(location.address)


