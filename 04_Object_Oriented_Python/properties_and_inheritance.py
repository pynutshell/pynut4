# calls base class method from property, even though
# method is overridden in derived class (property is
# defined using the base class method, and not resolved
# to the derived class method)
class B:
    def f(self):
        return 23
    g = property(f)
class C(B):
    def f(self):
        return 42
c = C()
print(c.g)                # prints: 23, not 42

# call subclass method from property by binding property
# to method that calls self.f(), to resolve to the derived
# class's method
class B:
    def f(self):
        return 23
    def _f_getter(self):
        return self.f()
    g = property(_f_getter)
class C(B):
    def f(self):
        return 42
c = C()
print(c.g)                # prints: 42, as expected
