class C5:
    def hello(self):
        print('Hello')

class C6:
    def __init__(self, n):
        self.x = n

another_instance = C6(42)

an_instance = C5()
an_instance.hello()                       # prints: Hello
print(another_instance.x)                 # prints: 42


class C7:
    pass
z = C7()
z.x = 23
print(z.x)                               # prints: 23

print(z.__class__.__name__, z.__dict__)    # prints: C7 {'x':23}

z.y = 45
z.__dict__['z'] = 67
print(z.x, z.y, z.z)                      # prints: 23 45 67

