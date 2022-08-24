# sample module, to be used to illustrate importing a module, and module-level __getattr__
from collections.abc import MutableSequence

def f():
    return None


def __getattr__(name):
    if name == 'first_10000_primes':
        import sys
        print(f"initializing {name}")
        # get current module object by looking up __name__ in sys.modules
        this_module = sys.modules[__name__]

        def generate_n_primes(n):
            found = [2]
            i = 3
            while len(found) < n:
                if not any(i % x == 0 for x in found):
                    found.append(i)
                i += 2
            return found

        this_module.first_10000_primes = generate_n_primes(10000)
        return this_module.first_10000_primes

    raise AttributeError(f'no such attribute {name!r}')
