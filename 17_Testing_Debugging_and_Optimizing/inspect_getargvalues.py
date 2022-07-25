import inspect

def f(x=23):
    return inspect.currentframe()

print(
    inspect.formatargvalues(
        *inspect.getargvalues(f())
    )
)
# prints: (x=23)
