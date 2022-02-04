class B:
    a = 23
    b = 45
    def f(self):
        print('method f in class B')
    def g(self):
        print('method g in class B')

class C(B):
    b = 67
    c = 89
    d = 123
    def g(self):
        print('method g in class C')
    def h(self):
        print('method h in class C')

b = B()
c = C()
for obj in (b, c):
    print(type(obj).__name__)
    print(f'obj.a = {getattr(obj, "a", "<not defined>")}')
    print(f'obj.b = {getattr(obj, "b", "<not defined>")}')
    print(f'obj.c = {getattr(obj, "c", "<not defined>")}')
    print(f'obj.d = {getattr(obj, "d", "<not defined>")}')
    print(f'obj.f() = {obj.f()}')
    print(f'obj.g() = {obj.g()}')
    print(f'obj.h() = {obj.h() if hasattr(obj, "h") else "<no such method h>"}')
    print()


