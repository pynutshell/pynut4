tree = (23, (42, (5, None, None), (55, None, None)), (94, None,None))

def rec(t):
    yield t[0]
    for i in (1, 2):
        if t[i] is not None:
            yield from rec(t[i])

for node in rec(tree):
    print(node)



def norec(t):
    stack = [t]
    while stack:
        t = stack.pop()
        yield t[0]
        for i in (2, 1):
            if t[i] is not None:
                stack.append(t[i])

for node in norec(tree):
    print(node)
