import dataclasses


@dataclasses.dataclass
class Point:
    x: float
    y: float


pt = Point(0.5, 0.5)
print(pt)
