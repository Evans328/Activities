import os
import requests
from dotenv import load_dotenv

# Load the API key from .env
load_dotenv()
api_key = os.getenv('API_KEY')

if api_key is None:
    print('API key not found - check that .env is in the same folder')
else:
    # St. Louis, Missouri coordinates
    
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {
        'lat': 38.627,
        'lon': -90.199,
        'appid': api_key,
        'units': 'imperial'      # Fahrenheit
    }

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code == 200:
        print('City:', data['name'], data['sys']['country'])
        print('City ID:', data['id'])
        print('Temperature:', data['main']['temp'], '°F')
        print('Feels like:', data['main']['feels_like'], '°F')
        print('Conditions:', data['weather'][0]['description'])
        print('Humidity:', data['main']['humidity'], '%')
        print('Wind:', data['wind']['speed'], 'mph')
    else:
        print('Error', response.status_code, '-', data.get('message'))