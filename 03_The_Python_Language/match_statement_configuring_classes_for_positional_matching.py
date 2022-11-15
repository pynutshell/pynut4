"""
>>> class Color:
...     __match_args__ = ('red', 'green', 'blue')
...     def __init__(self, r, g, b, name='anonymous'):
...         self.name = name
...         self.red, self.green, self.blue = r, g, b
...
>>> red_color = Color(255, 0, 0, 'red')
>>> blue_color = Color(0, 0, 255)
>>> for subject in (42.0, red_color, blue_color):
...     match subject:
...         case float(x):
...             print('float', x)
...         case Color(red, green, blue, name='red'):
...             print(type(subject).__name__, subject.name, red, green, blue)
...         case Color(a, b, 255) as bluish:
...             print(type(bluish).__name__, a, b, bluish.blue, bluish.name)
...         case _: print(type(subject), subject)
...
float 42.0
Color red 255 0 0
Color 0 0 255 anonymous
>>> match red:
...     case Color(1, 2, 3, 4): print("matched")
...
Traceback (most recent call last):
  ...
TypeError: Color() accepts 3 positional sub-patterns (4 given)
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
