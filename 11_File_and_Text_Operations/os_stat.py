import os
print(os.path.getsize(path))
print(os.stat(path)[6])
print(os.stat(path).st_size)
