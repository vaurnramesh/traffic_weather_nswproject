from dataclasses import dataclass
from typing import List
from .location import Location

@dataclass
class Trip:
    origin: Location
    destination: Location
    waypoints: List[Location] = None


    def get_all_points(self) -> List[Location]:
        """Returns all points that need a weather check."""
        points = [self.origin]
        if self.waypoints:
            points.extend(self.waypoints)
        points.append(self.destination)
        return points
