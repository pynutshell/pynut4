class Singleton:
    _singletons = {}

    def __new__(cls, *args, **kwds):
        if cls not in cls._singletons:
            cls._singletons[cls] = super().__new__(cls)
        return cls._singletons[cls]


# Singleton example - apologies to J.R.R. Tolkien

class RingOfPower:
    def __init__(self, ring_owner):
        self.owner = ring_owner
        self.bound_rings = []

    def bind_in_the_darkness(self):
        return self.bound_rings[:]

    def rules(self, rings):
        self.bound_rings.extend(rings)

    def __str__(self):
        return f'{id(self)}: {self.owner}'


class TheOneRing(Singleton, RingOfPower):
    def __init__(self):
        # guard against re-init on subsequent reference to singleton
        if getattr(self, "_TheOneRing__initialized", False):
            return
        self.__initialized = True
        super().__init__('The Dark Lord on His Dark Throne')


# The Rings of Power are created
elven_rings = [RingOfPower('Elven King Under The Sky') for _ in range(3)]
dwarven_rings = [RingOfPower('Dwarf Lord in Their Hall of Stone') for _ in range(7)]
mortal_men_rings = [RingOfPower('Mortal Man Doomed to Die') for _ in range(9)]
one_ring = TheOneRing()

# One Ring to rule them all
one_ring.rules(elven_rings)
one_ring.rules(dwarven_rings)
one_ring.rules(mortal_men_rings)

# list all the rings
for ring in one_ring.bind_in_the_darkness():
    print(ring)
print(one_ring)

# try to create another One Ring
another = TheOneRing()
print('one_ring', id(one_ring), id(one_ring.bound_rings))
print('another ', id(another), id(another.bound_rings))  # same id as for one_ring, and same instance var
print('They are the same ring', another is one_ring)     # prints True, they are the same object
