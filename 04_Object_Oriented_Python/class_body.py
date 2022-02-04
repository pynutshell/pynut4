
class C1:
    x = 23
print(C1.x)                            # prints: 23


class C2:
    pass
C2.x = 23
print(C2.x)                            # prints: 23


print(C1.__name__, C1.__bases__)


class C3:
    x = 23
    y = x + 22                          # must use just x, not C3.x


print(C3.x, C3.y)


class C4:
    x = 23
    def amethod(self):
        print(C4.x)  # must use C4.x or self.x, not just x!


C4().amethod()


class C5:
    def hello(self):
        print('Hello')


an_instance = C5()
an_instance.hello()


