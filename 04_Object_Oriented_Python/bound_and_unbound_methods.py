# excruciating low-level detail the conceptual steps involved in
# a method call with the normal syntax x.name(arg)
def f(a, b):
    '''a function f with two arguments'''
    print(a, b)
class C:
    name = f
x = C()

arg = 99
x.name(b=arg)
x.__class__.__dict__['name'](x, arg)


def make_adder_as_closure(augend):
    def add(addend, _augend=augend):
        return addend+_augend
    return add

def make_adder_as_bound_method(augend):
    class Adder:
        def __init__(self, augend):
            self.augend = augend
        def add(self, addend):
            return addend+self.augend
    return Adder(augend).add

def make_adder_as_callable_instance(augend):
    class Adder:
        def __init__(self, augend):
            self.augend = augend
        def __call__(self, addend):
            return addend+self.augend
    return Adder(augend)


fn = make_adder_as_closure(1000)
print(fn(1001))

fn = make_adder_as_bound_method(2000)
print(fn(1001))

fn = make_adder_as_callable_instance(3000)
print(fn(1001))
