"""
>>> import pathlib

>>> td = pathlib.Path("tempdir")
>>> sorted(td.glob('*'))
[WindowsPath('tempdir/bar'), WindowsPath('tempdir/foo')]
>>> sorted(td.glob('**/*'))
[WindowsPath('tempdir/bar'), WindowsPath('tempdir/bar/baz'), WindowsPath('tempdir/bar/boo'), WindowsPath('tempdir/foo')]
>>> sorted(td.glob('*/**/*'))    # expanding at 2nd+ level
[WindowsPath('tempdir/bar/baz'), WindowsPath('tempdir/bar/boo')]
>>> sorted(td.rglob('*'))        # just like glob('**/*')
[WindowsPath('tempdir/bar'), WindowsPath('tempdir/bar/baz'), WindowsPath('tempdir/bar/boo'), WindowsPath('tempdir/foo')]
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
