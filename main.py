from src.models.location import Location
from src.models.route import Trip
from src.models.bike import BikeProfile, BikeStyle
from src.clients.weather_api import WeatherApiClient
from src.service.ride_service import RideService

def main():
    # 1. Setup our "World"
    my_bike = BikeProfile(style=BikeStyle.NAKED) # Your MT-09 style
    
    # 2. Define a classic Sydney ride
    start = Location("Sydney CBD", -33.8688, 151.2093)
    mid = Location("Royal National Park", -34.1352, 151.0614)
    end = Location("Stanwell Tops", -34.2333, 150.9833)
    
    my_trip = Trip(origin=start, destination=end, waypoints=[mid])
    
    # 3. Initialize Services
    api_client = WeatherApiClient()
    service = RideService(api_client)
    
    # 4. Run the Pipeline
    print(f"--- 🏍️ Sydney Ride Report for {my_bike.style.value} Bike ---")
    reports = service.evaluate_trip(my_trip, my_bike)
    
    for report in reports:
        w = report.weather
        print(f"\n📍 {report.location_name}")
        print(f"   Score: {report.score}/10 | {report.verdict}")
        print(f"   Details: {w.temp_c}°C, Wind: {w.wind_gust_kmh}km/h, Rain: {w.rain_mm}mm")

if __name__ == "__main__":
    main()