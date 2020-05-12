#! python3
# getOpenWeather.py - Prints the weather for a location from the command line.

APPID = 'your APPID goes here'

import json
import requests
import sys

# Compute location from command line arguments.
if len(sys.argv) < 2:
    print('Usage: getOpenWeather.py city_name, 2-letter_country_code')
    sys.exit()
location = ','.join(sys.argv[1:])

# Download the JSON data from OpenWeatherMap.org's API.
url = f'https://api.openweathermap.org/data/2.5/weather?q={location}&units=metric&appid={APPID}'
response = requests.get(url)
response.raise_for_status()

# Uncomment to see the raw JSON text:
print(response.text)

# Load JSON data into a Python variable.
weatherData = json.loads(response.text)

# Print weather descriptions.
w = weatherData
print(f'Current weather in {location}')
print(w['weather'][0]['main'], '-', w['weather'][0]['description'])
