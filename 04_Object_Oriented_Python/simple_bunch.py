class SimpleBunch:
    def __init__(self, **fields):
        self._dict__ = fields


p = SimpleBunch(x=2.3, y=4.5)
print(p)


