from dataclasses import dataclass
from src.models.weather import WeatherObservation

@dataclass
class RideEvaluation:
    location_name: str
    score: float
    weather: WeatherObservation
    verdict: str