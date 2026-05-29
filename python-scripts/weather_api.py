"""
Weather API — Current "feels like" temperature via OpenWeatherMap
Requires WEATHER_APP_KEY in .env (get one free at openweathermap.org/api)
"""

import os
import requests
from dotenv import load_dotenv

load_dotenv(override=True)

# Default coordinates: New Jersey area
DEFAULT_LAT = 40.62094138455799
DEFAULT_LON = -74.7644006535796


def get_weather(lat: float, lon: float) -> dict:
    api_key = os.getenv("WEATHER_APP_KEY")
    if not api_key:
        raise ValueError("WEATHER_APP_KEY not set in .env")

    url = (
        f"https://api.openweathermap.org/data/2.5/forecast"
        f"?units=metric&cnt=1&lat={lat}&lon={lon}&appid={api_key}"
    )
    response = requests.get(url)
    response.raise_for_status()
    return response.json()


if __name__ == "__main__":
    data = get_weather(DEFAULT_LAT, DEFAULT_LON)
    feels_like = data["list"][0]["main"]["feels_like"]
    city = data["city"]["name"]
    print(f"Currently feels like {feels_like}°C in {city}.")
