from dataclasses import dataclass, field

@dataclass
class PenaltyThreshold:
    limit: float
    penalty: float

@dataclass
class WeatherConfig:
    WIND_CRITICAL: float = 75.0
    WIND_HIGH: PenaltyThreshold = field(
        default_factory=lambda: PenaltyThreshold(45.0, 4.0)
    )
    WIND_MEDIUM: PenaltyThreshold = field(
        default_factory=lambda: PenaltyThreshold(30.0, 2.0)
    )

    RAIN_HEAVY: PenaltyThreshold = field(
        default_factory=lambda: PenaltyThreshold(10.0, 5.0)
    )
    RAIN_MODERATE: PenaltyThreshold = field(
        default_factory=lambda: PenaltyThreshold(3.0, 2.0)
    )
    RAIN_PROB_THRESHOLD: int = 30

    TEMP_FREEZING: PenaltyThreshold = field(
        default_factory=lambda: PenaltyThreshold(10.0, 2.5)
    )
    TEMP_SCORCHING: PenaltyThreshold = field(
        default_factory=lambda: PenaltyThreshold(38.0, 3.5)
    )