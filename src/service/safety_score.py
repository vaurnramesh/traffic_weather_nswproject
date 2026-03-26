from src.models.bike import BikeProfile
from src.models.weather import WeatherObservation
from src.models.config import WeatherConfig

def calculate_ride_score(bike: BikeProfile, weather: WeatherObservation, config: WeatherConfig = None) -> float:

    score = 10.0
    if config is None:
        config = WeatherConfig() # to keep the config clean after further mutations

    impact_gust = weather.wind_gust_kmh * bike.style.wind_sensitivity_factor

    match impact_gust:
        case g if g > config.WIND_CRITICAL:
            return 0.0
        case g if g > config.WIND_HIGH.limit:
            score -= config.WIND_HIGH.penalty
        case g if g > config.WIND_MEDIUM.limit:
            score -= config.WIND_MEDIUM.penalty
        
    match (weather.rain_mm, weather.precipitation_prob):
        case (r, _) if r > config.RAIN_HEAVY.limit:
            score -= config.RAIN_HEAVY.penalty
        case (r, p) if r > config.RAIN_MODERATE.limit or p > config.RAIN_PROB_THRESHOLD:
            score -= config.RAIN_MODERATE.penalty
        case _:
            pass


    match weather.temp_c:
        case t if t < config.TEMP_FREEZING.limit:
            score -= config.TEMP_FREEZING.penalty
        case t if t > config.TEMP_SCORCHING.limit:
            score -= config.TEMP_SCORCHING.penalty

    return round(max(0.0, score), 1)

    
    
