"""
>>> import pathlib
>>> p = pathlib.Path('p.txt')
>>> t = pathlib.Path('testfile.txt')


>>> p.read_text()
'spam'
>>> t.read_text()
'and eggs'
>>> p.replace(t)
WindowsPath('testfile.txt')
>>> t.read_text()
'spam'
>>> p.read_text()
Traceback (most recent call last):
...
FileNotFoundError: [Errno 2] No such file…
"""