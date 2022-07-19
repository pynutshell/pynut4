S = set([1, 2, 3])
# destructive loop
while S:
    item = S.pop()
    # ...handle item...

# non-destructive loop
for item in S:
    # ...handle item...
    pass

