from dotenv import load_dotenv
from pprint import pprint
import requests
import os
import certifi
 
load_dotenv()  # to load API_KEY from .env file

def get_current_weather(city="Bangalore"):
    requests_url = "https://api.openweathermap.org/data/2.5/weather?appid={os.getenv('API_KEY')}&q={city}&units=metric"

    weather_data = requests.get(requests_url).json()
    return weather_data

if __name__ == "__main__":
    print("\n***** Get Weather Condition ☁️ ⛅ ⛈️ 🌩️ 🌦️ *****\n")
    city = input("\nPlease enter a city name : ")
    #Check for empty string or string with only spaces
    #if not bool(city.strip()):

    weather_data = get_current_weather(city)

    print("\n")
    pprint(weather_data)
