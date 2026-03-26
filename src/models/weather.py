from dataclasses import dataclass, field
from datetime import datetime

@dataclass
class AuditMetadata:
    """Internal tracking for our Data Lake (The 'Who/When/How')"""
    fetched_at: datetime = field(default_factory=datetime.now)
    is_forecast: bool = False
    source: str = "open-meteo"

@dataclass
class WeatherObservation:
    """The actual state of the world (The 'What/Where')"""
    location_name: str
    timestamp: datetime
    temp_c: float
    wind_gust_kmh: float
    rain_mm: float
    precipitation_prob: int
    metadata: AuditMetadata = field(default_factory=AuditMetadata)