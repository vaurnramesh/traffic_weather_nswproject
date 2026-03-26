from dataclasses import dataclass, field
from src.models.weather import WeatherObservation

@dataclass
class ScoreResult:
    """The raw output of our safety heuristic."""
    score: float
    reasons: list[str] = field(default_factory=list)

@dataclass
class RideEvaluation:
    location_name: str
    weather: WeatherObservation
    verdict: str
    analysis: ScoreResult