class keydefaultdict(dict):
    def __init__(self, default_factory=None, *a, **k):
        super().__init__(*a, **k)
        self.default_factory = default_factory
    def __missing__(self, key):
        if self.default_factory is None:
            raise KeyError(key)
        self[key] = self.default_factory(key)
        return self[key]


# cannot use collections defaultdict with CustomerTally, since it takes an __init__ argument
class CustomerTally:
    def __init__(self, postal_code):
        self.postal_code = postal_code
        self._customers = set()
    def add_customer(self, name):
        self._customers.add(name)
    @property
    def customers(self):
        return sorted(self._customers)


# tally customers by postal code
tally = keydefaultdict(CustomerTally)
for nm, code in [
    ('Alice', '12345'),
    ('Bob', '00123'),
    ('Alice', '00123')
]:
    tally[code].add_customer(nm)

for customers_by_code in tally.values():
    print(f'{customers_by_code.postal_code} - {len(customers_by_code.customers)}')
