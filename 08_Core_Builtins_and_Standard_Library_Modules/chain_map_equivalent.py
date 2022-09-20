import collections


class ChainMap(collections.abc.MutableMapping):
    def __init__(self, *maps):
        self.maps = list(maps)
        self._keys = set()
        for m in self.maps:
            self._keys.update(m)
    def __len__(self): return len(self._keys)
    def __iter__(self): return iter(self._keys)
    def __getitem__(self, key):
        if key not in self._keys: raise KeyError(key)
        for m in self.maps:
            try: return m[key]
            except KeyError: pass
    def __setitem__(self, key, value):
        self.maps[0][key] = value
        self._keys.add(key)
    def __delitem__(self, key):
        del self.maps[0][key]
        self._keys = set()
        for m in self.maps:
            self._keys.update(m)


# uncomment this line to compare the above class with the actual collections.ChainMap
# from collections import ChainMap

args = {'a': 100, 'b': 101}
defaults = {'a': 1, 'b': 2, 'c': 3}

cm = ChainMap(args, defaults)
print(list(cm))
print(list(cm.items()))

