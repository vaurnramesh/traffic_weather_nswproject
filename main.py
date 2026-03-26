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
    mid = Location("Parramatta", -33.8148, 151.0017)
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
        print(f"   Score: {report.analysis.score}/10 | {report.verdict}")
        print(f"   Details: {w.temp_c}°C, Wind: {w.wind_gust_kmh}km/h, Rain: {w.rain_mm}mm")
        if report.analysis.reasons:
            print(f"   ⚠️  {', '.join(report.analysis.reasons)}")

        print("\n" + "="*50)

    # 5. Run the Forecast Pipeline
    print(f"--- 📅 Sydney 24-Hour FORECAST (Best Windows) ---")
    forecast_matrix = service.evaluate_trip_forecast(my_trip, my_bike)
    
    for location_name, hourly_reports in forecast_matrix.items():
        print(f"\n📍 {location_name}")
        
        # Sort by score to find the top 3 hours for this specific location
        top_windows = sorted(hourly_reports, key=lambda x: x.analysis.score, reverse=True)[:10]
        
        for report in top_windows:
            w = report.weather
            # Extracting HH:MM from ISO timestamp (e.g. 2026-03-26T14:00)
            time_label = w.timestamp.split("T")[-1]
            
            print(f"   🕒 {time_label} | Score: {report.analysis.score}/10 | {report.verdict}")
            if report.analysis.reasons:
                 print(f"      Reasons: {', '.join(report.analysis.reasons)}")

if __name__ == "__main__":
    main()