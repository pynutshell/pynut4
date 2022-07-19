import tempfile, shutil

path = tempfile.mkdtemp()
try:
    use_dirpath(path)
finally:
    shutil.rmtree(path)


import tempfile, os
fd, path = tempfile.mkstemp(suffix='.txt', text=True)
try:
    os.close(fd)
    use_filepath(path)
finally:
    os.unlink(path)


