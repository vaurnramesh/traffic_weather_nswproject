from src.models.location import Location
from src.models.route import Trip
from src.models.bike import BikeProfile, BikeStyle
from src.clients.weather_api import WeatherApiClient
from src.service.ride_service import RideService
from src.service.reporter import RideReporter

def main():
    # 1. Setup
    my_bike = BikeProfile(style=BikeStyle.NAKED)
    api_client = WeatherApiClient()
    service = RideService(api_client)
    reporter = RideReporter()
    
    # 2. Trip Definition
    my_trip = Trip(
        origin=Location("Sydney CBD", -33.8688, 151.2093),
        destination=Location("Stanwell Tops", -34.2333, 150.9833),
        waypoints=[Location("Parramatta", -33.8148, 151.0017)]
    )
    
    # 3. Execution & Reporting
    # Current Weather
    current_results = service.evaluate_trip(my_trip, my_bike)
    reporter.generate_current_report(current_results)
    
    # Forecasted Weather
    forecast_matrix = service.evaluate_trip_forecast(my_trip, my_bike)
    
    # Best Windows
    reporter.generate_forecast_summary(forecast_matrix, mode="best")
    
    # Avoid Windows
    reporter.generate_forecast_summary(forecast_matrix, mode="avoid")

if __name__ == "__main__":
    main()