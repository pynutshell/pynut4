"""
>>> object().__format__('')
'<object object at 0x110045070>'
>>> import math
>>> math.pi.__format__('18.6')
'           3.14159'

>>> class S:
...     def __init__(self, value):
...         self.value = value
...     def __format__(self, fstr):
...         match fstr:
...             case "U":
...                 return self.value.upper()
...             case 'L':
...                 return self.value.lower()
...             case 'T':
...                 return self.value.title()
...             case _:
...                 return ValueError(f'Unrecognised format code {fstr!r}')
...
>>> my_s = S('random string')
>>> f'{my_s:L}, {my_s:U}, {my_s:T}'
'random string, RANDOM STRING, Random String'

>>> import datetime
>>> d = datetime.datetime.now()
>>> d.__format__("%d/%m/%y")
'10/04/22'
>>> "{:%d/%m/%y}".format(d)
'10/04/22'
>>> f"{d:%d/%m/%y}"  # See “Formatted String Literals”
'10/04/22'

"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod()
