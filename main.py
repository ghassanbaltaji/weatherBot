import requests

OPENWEATHERMAP_API_KEY = 'Your Public Key' # You can get the public key from the 'OpenWeatherMap' site
OPENWEATHERMAP_API_URL = 'http://api.openweathermap.org/data/2.5/weather'

def get_weather(city):
    params = {
        'q': city,
        'appid': OPENWEATHERMAP_API_KEY,
        'units': 'metric',
    }
    response = requests.get(OPENWEATHERMAP_API_URL, params=params)
    data = response.json()

    if response.status_code == 200:
        weather_info = data.get('weather', [{}])[0].get('description', 'unknown')
        temperature = data.get('main', {}).get('temp', 'unknown')
        return f"The weather in {city} is {weather_info} with a temperature of {temperature}°C."
    else:
        error_message = data.get('message', 'Unknown error')
        return f"Sorry, could not retrieve weather information for {city}. Error: {error_message}"

# Example usage
city_to_check = "Oslo"
weather_result = get_weather(city_to_check)
print(weather_result)
