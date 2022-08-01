import math

_sin_degrees_lookup = {x: math.sin(math.radians(x)) for x in range(0, 360+1)}
sin_degrees = _sin_degrees_lookup.__getitem__
