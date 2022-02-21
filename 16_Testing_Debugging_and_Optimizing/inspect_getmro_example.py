import inspect

class A: pass
class B(A): pass
class C(A): pass
class D(B, C): pass
for c in inspect.getmro(D):
    print(c.__name__, end=' ')
