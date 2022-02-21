import inspect
def a():
    for frame in inspect.stack():
        print(frame)

def b():
    a()

def c():
    b()

c()
