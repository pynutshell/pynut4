_count = 0
def counter():
    global _count
    _count += 1
    return _count

for i in range(10):
    print(i, counter())
