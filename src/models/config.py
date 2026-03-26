from dataclasses import dataclass, field

@dataclass
class Penalty:
    limit: float
    deduction: float

@dataclass
class WeatherConfig:
    # WIND: More steps for gradual score decay
    WIND_STAGES: list[Penalty] = field(default_factory=lambda: [
        Penalty(70.0, 10.0), # Critical - No ride
        Penalty(55.0, 5.0),  # Very High
        Penalty(40.0, 3.0),  # High
        Penalty(25.0, 1.5),  # Moderate
        Penalty(15.0, 0.5),  # Light breeze (slight penalty for Naked bikes)
    ])

    # RAIN: Differentiate between "Damp" and "Flood"
    RAIN_PROB_THRESHOLD: int = 30
    RAIN_STAGES: list[Penalty] = field(default_factory=lambda: [
        Penalty(15.0, 6.0),  # Torrential
        Penalty(8.0, 4.0),   # Heavy
        Penalty(4.0, 2.0),   # Consistent Rain
        Penalty(1.0, 1.0),   # Showers/Drizzle
    ])

    # TEMPERATURE: Comfort curves
    COLD_STAGES: list[Penalty] = field(default_factory=lambda: [
        Penalty(5.0, 4.0),   # Freezing
        Penalty(12.0, 2.0),  # Cold
        Penalty(18.0, 0.5),  # Crisp (Minor penalty for tire warm-up)
    ])

    HOT_STAGES: list[Penalty] = field(default_factory=lambda: [
        Penalty(40.0, 5.0),  # Extreme Heat - Danger of heatstroke/dehydration
        Penalty(35.0, 3.0),  # Very Hot - High fatigue, tires get greasy
        Penalty(30.0, 1.0),  # Warm - Start carrying extra water
    ])