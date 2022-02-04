class Base:
    def greet(self, name):
        print('Welcome', name)

class Sub(Base):
    def greet(self, name):
        print('Well Met and', end=' ')
        Base.greet(self, name)

x = Sub()
x.greet('Alex')


class Base:
    def __init__(self):
        self.anattribute = 23

# this form (calling Base explicitly) is not encouraged
class Derived(Base):
    def __init__(self):
        Base.__init__(self)
        self.anotherattribute = 45

# using super() is the preferred form
class Derived(Base):
    def __init__(self):
        super().__init__()
        self.anotherattribute = 45

z = Derived()
print(vars(z))
