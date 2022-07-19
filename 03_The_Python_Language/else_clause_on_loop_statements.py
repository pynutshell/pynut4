some_container = list(range(5))

def is_ok(i):
    return i > 10


for x in some_container:
    if is_ok(x):
        break  # item x is satisfactory, terminate loop
else:
    print('Beware: no satisfactory item was found in container')
    x = None
