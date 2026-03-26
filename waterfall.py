import requests
import json

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": -33.8688,
    "longitude": 151.2093,
    "hourly": [
        "temperature_2m", 
        "precipitation", 
        "rain", 
        "precipitation_probability",
        "wind_speed_10m",
        "wind_gusts_10m"
    ],
    "timezone": "Australia/Sydney",
    "forecast_days": 2
}

try:
    response = requests.get(url, params=params)
    response.raise_for_status() # This stops the script if the API is down
    data = response.json()
    print(json.dumps(data, indent=4))

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")