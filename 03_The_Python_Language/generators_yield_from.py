def updown(N):
    yield from range(1, N)
    yield from range(N, 0, -1)

for i in updown(3):
    print(i)                   # prints: 1 2 3 2 1
