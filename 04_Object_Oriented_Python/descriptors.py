class Const:  # an overriding descriptor, see later
    def __init__(self, value):
        self.value = value

    def __set__(self, *_):  # silently ignore any attempt at setting
        pass

    def __get__(self, *_):  # always return the constant value
        return self.value

    def __delete__(self, *_):  # const cannot be deleted
        pass


class X:
    c = Const(23)


x = X()
print(x.c)  # prints: 23
x.c = 42  # silently ignored
print(x.c)  # prints: 23
del x.c
print(x.c)  # prints: 23

