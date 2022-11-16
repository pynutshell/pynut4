"""
>>> import pathlib
>>>
>>> td=pathlib.Path('tempdir/')
>>> td.mkdir()
>>> td.is_dir()
True
>>> td.resolve()
WindowsPath('C:/Users/annar/tempdir')
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
