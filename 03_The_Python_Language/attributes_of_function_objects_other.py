def counter():
    counter.count += 1
    return counter.count
counter.count = 0


for i in range(10):
    print(i, counter())
