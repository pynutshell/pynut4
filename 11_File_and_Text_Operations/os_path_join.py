import os

print(os.path.join('a/b', 'c/d', 'e/f'))
   # on Unix prints: a/b/c/d/e/f
print(os.path.join('a/b', '/c/d', 'e/f'))
   # on Unix prints: /c/d/e/f
