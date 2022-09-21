import warnings


def to_unicode(bytestr):
    try:
        return bytestr.decode()
    except UnicodeError:
        warnings.warn(f'Invalid characters in {bytestr!r}',
                      stacklevel=2)
        return bytestr.decode(errors='ignore')


# call to_unicode with invalid characters, warning will point to this line
to_unicode(b'ABC\xff\xfeDEF')
