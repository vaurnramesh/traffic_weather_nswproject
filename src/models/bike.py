from dataclasses import dataclass
from enum import Enum

class BikeStyle(Enum):
    NAKED = "Naked"                 # High wind sensitivity
    FULL_FAIRED = "Sport"           # Better aero, but can act like a sail in crosswinds
    CRUISER = "Cruiser"             # Usually heavy, low center of gravity
    ADVENTURE = "ADV"               # Tall, high wind profile 

    @property
    def wind_sensitivity_factor(self) -> float:
        """
        Infer sensitivity based purely on category.
        1.0 = Baseline
        """
        factors = {
            BikeStyle.CRUISER: 1.0,
            BikeStyle.ADVENTURE: 1.1,
            BikeStyle.FULL_FAIRED: 1.3,
            BikeStyle.NAKED: 1.5
        }
        return factors.get(self, 1.0)
    
@dataclass
class BikeProfile:
    style: BikeStyle