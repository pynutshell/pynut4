import math
def sin_degrees(x):
    return math.sin(math.radians(x))

# function with unbounded memoizing cache
cached_values = {}
def sin_degrees(x):
    if x not in cached_values:
        cached_values[x] = math.sin(math.radians(x))
    return cached_values[x]

# same function, with _cached_values defined as an attribute
def sin_degrees(x):
    cache = sin_degrees._cached_values
    if x not in cache:
        cache[x] = math.sin(math.radians(x))
    return cache[x]
sin_degrees._cached_values = {}

# function with bounded FIFO memoizing cache
def sin_degrees(x):
    cache = sin_degrees._cached_values
    if x not in cache:
        cache[x] = math.sin(math.radians(x))
        # remove oldest cache entry if exceed maxsize limit
        if len(cache) > sin_degrees._maxsize:
            oldest_key = next(iter(cache))
            del cache[oldest_key]
    return cache[x]
sin_degrees._cached_values = {}
sin_degrees._maxsize = 512

# function with bounded LRU cache
import functools
@functools.lru_cache(maxsize=512)
def sin_degrees(x):
    return math.sin(math.radians(x))
