from src.models.bike import BikeProfile
from src.models.weather import WeatherObservation
from src.models.config import WeatherConfig

def calculate_ride_score(bike: BikeProfile, weather: WeatherObservation, config: WeatherConfig = WeatherConfig()) -> float:

    score = 10.0
    
    # 1. Wind Calculation
    impact_gust = weather.wind_gust_kmh * bike.style.wind_sensitivity_factor
    for stage in config.WIND_STAGES:
        if impact_gust >= stage.limit:
            score -= stage.deduction
            break # Apply only the harshest applicable penalty

    # 2. Rain Calculation
    # We only check rain if there's actual moisture OR high probability
    if weather.rain_mm > 0 or weather.precipitation_prob > config.RAIN_PROB_THRESHOLD:
        for stage in config.RAIN_STAGES:
            if weather.rain_mm >= stage.limit:
                score -= stage.deduction
                break

    # 3. Temperature Calculation (Cold & Hot)
    temp = weather.temp_c
    
    # Check for Cold (Lower than limit)
    for stage in config.COLD_STAGES:
        if temp <= stage.limit:
            score -= stage.deduction
            break # Apply harshest cold penalty

    # Check for Hot (Higher than limit)
    for stage in config.HOT_STAGES:
        if temp >= stage.limit:
            score -= stage.deduction
            break # Apply harshest heat penalty

    return round(max(0.0, score), 1)

    
    
