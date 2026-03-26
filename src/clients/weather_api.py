import requests
from src.models.location import Location
from src.models.weather import WeatherObservation, AuditMetadata

class WeatherApiClient:
    def __init__(self):
        self.base_url = "https://api.open-meteo.com/v1/forecast"

    def fetch_current_weather(self, location: Location) -> WeatherObservation:

        params = {
            "latitude": location.latitude,
            "longitude": location.longitude,
            "current": ["temperature_2m", "wind_gusts_10m", "rain", "precipitation_probability"],
            "timezone": "Australia/Sydney"
        }

        response = requests.get(self.base_url, params=params)
        response.raise_for_status()
        data = response.json()
        curr = data['current']

        return WeatherObservation(
            location_name=location.name,
            timestamp=curr['time'],
            temp_c=curr['temperature_2m'],
            wind_gust_kmh=curr['wind_gusts_10m'],
            rain_mm=curr['rain'],
            precipitation_prob=curr['precipitation_probability'],
            metadata=AuditMetadata(is_forecast=False)
        )
