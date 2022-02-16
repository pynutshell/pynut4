class A:
    def ff(self):
        pass

x = A()

try:
    x.f()
except AttributeError:
    import sys, inspect
    print(f'x is type {type(x)}, ({x!r})', file=sys.stderr)
    print("x's methods are:", file=sys.stderr, end='')
    for n, v in inspect.getmembers(x, callable):
        print(n, file=sys.stderr, end=' ')
    print(file=sys.stderr)
    raise

# The function getmembers of the module inspect obtains the name of all the methods
# available on x in order to display them. If you need this kind of diagnostic functionality
# often, package it up into a separate function, such as:
import sys, inspect
def show_obj_methods(obj, name, show=sys.stderr.write):
    show(f'{name} is type {type(obj)}({obj!r})\n')
    show(f"{name}'s methods are: ")
    for n, v in inspect.getmembers(obj, callable):
       show(f'{n} ')
    show('\n')

# And then the example becomes just:
try:
    x.f()
except AttributeError:
    show_obj_methods(x, 'x')
    raise
