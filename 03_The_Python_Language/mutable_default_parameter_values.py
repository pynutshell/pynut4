def f(x, y=[]):
    y.append(x)
    return id(y), y

print(f(23))             # prints: (4302354376, [23])
z = []
print(f(42))             # prints: (4302354376, [23, 42])


def f(x, y=None):
    if y is None:
        y = []
    y.append(x)
    return id(y), y

print(f(23))             # prints: (4302354376, [23])
z = []                   # force creation of object between calls so id's don't get reused
# print(id(z))
print(f(42))             # prints: (4302180040, [42])



def costly_computation(a):
    print(f"compute using {a}")
    return a * a

def cached_compute(x, _cache={}):
    if x not in _cache:
        _cache[x] = costly_computation(x)
    return _cache[x]


print(cached_compute(100))
print(cached_compute(200))
print(cached_compute(100))
