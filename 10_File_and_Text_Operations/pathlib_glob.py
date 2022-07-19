"""
import pathlib

>>> sorted(td.glob('*'))
[WindowsPath('tempdir/bar'), WindowsPath('tempdir/foo')]
>>> sorted(td.glob('**/*'))
[WindowsPath('tempdir/bar'), WindowsPath('tempdir/bar/baz'), WindowsPath('tempdir/bar/boo'), WindowsPath('tempdir/foo')]
>>> sorted(td.glob('*/**/*'))    # expanding at 2nd+ level
[WindowsPath('tempdir/bar/baz'), WindowsPath('tempdir/bar/boo')]
>>> sorted(td.rglob('*'))        # just like glob('**/*')
[WindowsPath('tempdir/bar'), WindowsPath('tempdir/bar/baz'), WindowsPath('tempdir/bar/boo'), WindowsPath('tempdir/foo')]
"""
