import math
def sin_degrees(x):
    return math.sin(math.radians(x))

# function with unbounded memoizing cache
cached_values = {}
def sin_degrees(x):
    if x not in cached_values:
        cached_values[x] = math.sin(math.radians(x))
    return cached_values[x]

# function with bounded FIFO memoizing cache
cached_values = {}
maxsize = 64
def sin_degrees(x):
    if x not in cached_values:
        cached_values[x] = math.sin(math.radians(x))
        if len(cached_values) > maxsize:
            oldest_key = next(iter(cached_values))
            del cached_values[oldest_key]
    return cached_values[x]

# function with bounded LRU cache
import functools
@functools.lru_cache(maxsize=64)
def sin_degrees(x):
    return math.sin(math.radians(x))
