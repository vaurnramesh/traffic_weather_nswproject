from typing import List, Dict
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

        location_reports = []

        for location in trip.get_all_points():
            weather_data = self.client.fetch_current_weather(location)
            analysis = calculate_ride_score(bike, weather_data)
            verdict = "SEND IT" if analysis.score >= 7.5 else "CAUTION" if analysis.score >= 5 else "STAY HOME"

            location_reports.append(RideEvaluation(
                location_name=location.name,
                weather=weather_data,
                verdict=verdict,
                analysis=analysis
            ))
            
        return location_reports
    
    def evaluate_trip_forecast(self, trip: Trip, bike: BikeProfile) -> Dict[str, List[RideEvaluation]]:
        
        forecast_matrix = {}

        for location in trip.get_all_points():
            location_reports = []
            hourly_weather = self.client.fetch_hourly_forecast(location, 1)
            
            for weather_data in hourly_weather:
                analysis = calculate_ride_score(bike, weather_data)
                verdict = "SEND IT" if analysis.score >= 7.5 else "CAUTION" if analysis.score >= 5 else "STAY HOME"

                location_reports.append(RideEvaluation(
                    location_name=location.name,
                    weather=weather_data,
                    verdict=verdict,
                    analysis=analysis
                ))
            forecast_matrix[location.name] = location_reports

        return forecast_matrix
