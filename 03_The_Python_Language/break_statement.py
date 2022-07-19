i = -5
def get_next():
    global i
    i += 1
    return i

def preprocess(i):
    return i * i

def keep_looping(a, b):
    return a != b

def process(a, b):
    x = a ** b
    print(a, b, x)


while True:          # this loop can never terminate “naturally”
    x = get_next()
    y = preprocess(x)
    if not keep_looping(x, y):
        break
    process(x, y)

