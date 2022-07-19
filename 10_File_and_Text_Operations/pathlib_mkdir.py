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