"""
>>> from pathlib import Path

>>> d
WindowsPath('C:/Users/annar/Documents')
>>> f = Path(d) / 'testfile.txt'
>>> f.is_file()
False
>>> f.touch()
>>> f.is_file()
True
"""