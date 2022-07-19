import os
import errno

try:
    os.some_os_function_or_other()
except FileNotFoundError as err:
    print('Warning: file', err.filename, 'not found; continuing')
except OSError as oserr:
    print(f'Error {errno.errorcode[oserr.errno]}; continuing')
