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

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
