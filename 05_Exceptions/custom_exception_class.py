import warnings

class InvalidAttribute(AttributeError):
    """Used to indicate attributes that could never be valid"""

class SomeFunkyClass:
    """much hypothetical functionality snipped"""
    def __getattr__(self, name):
        """only clarifies the kind of attribute error"""
        if name.startswith('_'):
            raise InvalidAttribute(f'Unknown private attribute {name!r}')
        else:
            raise AttributeError(f'Unknown attribute {name!r}')

s = SomeFunkyClass()

for thename in ('_abc', 'def'):
    try:
        value = getattr(s, thename)
    except InvalidAttribute as err:
        warnings.warn(str(err), stacklevel=2)
        value = None
