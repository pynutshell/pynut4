import contextlib

@contextlib.contextmanager
def tag(tagname):
    print(f'<{tagname}>', end='')
    try:
        yield
    finally:
        print(f'</{tagname}>')

tt = tag('sometag')
with tt:
    print('some output')