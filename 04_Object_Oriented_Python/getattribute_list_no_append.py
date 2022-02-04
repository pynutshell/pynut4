class listNoAppend(list):
    def __getattribute__(self, name):
        if name == 'append':
            raise AttributeError(name)
        return list.__getattribute__(self, name)

lna = listNoAppend([1, 2, 3])
lna.extend([4, 5, 6])
print(lna)

# raises AttributeError
lna.append(7)
