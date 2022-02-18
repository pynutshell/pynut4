import dataclasses
import time
import math


@dataclasses.dataclass
class Point:
    x: float
    y: float
    create_time: float = 0

    def __post_init__(self):
        self.create_time = time.time()

    def distance_from(self, other: "Point"):
        dx, dy = self.x - other.x, self.y - other.y
        return math.hypot(dx, dy)

    @property
    def distance_from_origin(self):
        return self.distance_from(Point(0, 0))


pt = Point(0.5, 0.5)

# will print members, but not properties
print(pt)

print(f"{pt.distance_from(Point(-1, -1))}")
print(f"{pt.distance_from_origin}")
