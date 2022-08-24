import sys

import mymodule
a = mymodule.f()


import mymodule as alias
a = alias.f()


# get dynamically generated attribute
print(f'10,000th prime is {mymodule.first_10000_primes[-1]}')

def find_prime_triples():
    for a, b, c in zip(mymodule.first_10000_primes,
                       mymodule.first_10000_primes[1:],
                       mymodule.first_10000_primes[2:]):
        if c-a == 6:
            yield a, b, c

for x in find_prime_triples():
    print(x)

print(dir(mymodule))
