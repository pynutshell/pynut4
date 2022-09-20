# equivalent behavior to collections.defaultdict
class defaultdict(dict):
    def __init__(self, default_factory=None, *a, **k):
        super().__init__(*a, **k)
        self.default_factory = default_factory
    def __getitem__(self, key):
        if key not in self and self.default_factory is not None:
            self[key] = self.default_factory()
        return dict.__getitem__(self, key)


# uncomment this line to compare with actual collections.defaultdict
from collections import defaultdict

dd = defaultdict(lambda: None, a=10, b=20)
print(dd['a'])
print(dd['c'])
