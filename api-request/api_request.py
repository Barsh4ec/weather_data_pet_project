import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("API_KEY")
api_url = f"https://api.weatherstack.com/current?access_key={api_key}&query=Lviv"

def fetch_data():

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        print("API response received successfully")
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        raise


def mock_fetch_data():
    return {'request': {'type': 'City', 'query': 'New York, United States of America', 'language': 'en', 'unit': 'm'}, 'location': {'name': 'New York', 'country': 'United States of America', 'region': 'New York', 'lat': '40.714', 'lon': '-74.006', 'timezone_id': 'America/New_York', 'localtime': '2026-04-01 11:14', 'localtime_epoch': 1775042040, 'utc_offset': '-4.0'}, 'current': {'observation_time': '03:14 PM', 'temperature': 22, 'weather_code': 113, 'weather_icons': ['https://cdn.worldweatheronline.com/images/wsymbols01_png_64/wsymbol_0001_sunny.png'], 'weather_descriptions': ['Sunny'], 'astro': {'sunrise': '06:39 AM', 'sunset': '07:21 PM', 'moonrise': '07:14 PM', 'moonset': '06:14 AM', 'moon_phase': 'Waxing Gibbous', 'moon_illumination': 99}, 'air_quality': {'co': '190.85', 'no2': '18.55', 'o3': '81', 'so2': '7.95', 'pm2_5': '9.25', 'pm10': '9.45', 'us-epa-index': '1', 'gb-defra-index': '1'}, 'wind_speed': 14, 'wind_degree': 265, 'wind_dir': 'W', 'pressure': 1017, 'precip': 0, 'humidity': 53, 'cloudcover': 0, 'feelslike': 25, 'uv_index': 4, 'visibility': 16, 'is_day': 'yes'}}
