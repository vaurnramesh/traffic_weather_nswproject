from typing import List
from src.models.route import Trip
from src.models.bike import BikeProfile
from src.models.evaluation import RideEvaluation
from src.clients.weather_api import WeatherApiClient
from src.service.safety_score import calculate_ride_score

class RideService:
    def __init__(self, weather_client: WeatherApiClient):
        self.client = weather_client

    def evaluate_trip(self, trip: Trip, bike: BikeProfile) -> List[RideEvaluation]:
        """
        Loops through all points in a trip and generates a safety report.
        """

        evaluations = []

        for location in trip.get_all_points():

            weather_data = self.client.fetch_current_weather(location)

            score = calculate_ride_score(bike, weather_data)

            verdict = "SEND IT" if score >= 7.5 else "CAUTION" if score >= 5 else "STAY HOME"

            evaluations.append(RideEvaluation(
                location_name=location.name,
                score=score,
                weather=weather_data,
                verdict=verdict
            ))
            
        return evaluations