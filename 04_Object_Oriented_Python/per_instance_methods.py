def fake_get_item(idx):
    return idx

class MyClass:
    pass

n = MyClass()

# add a method to n and call it
n.instance_method = fake_get_item
print(n.instance_method(100))

# special methods cannot be added per-instance
n.__getitem__ = fake_get_item
print(n[23])                      # raises TypeError