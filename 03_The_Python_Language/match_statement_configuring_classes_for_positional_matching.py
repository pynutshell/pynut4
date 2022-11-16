"""
>>> class Color:
...     __match_args__ = ('red', 'green', 'blue')
...     def __init__(self, r, g, b, name='anonymous'):
...         self.name = name
...         self.red, self.green, self.blue = r, g, b
...
>>> color_red = Color(255, 0, 0, 'red')
>>> color_blue = Color(0, 0, 255)
>>> for subject in (42.0, color_red, color_blue):
...     match subject:
...         case float(x):
...             print('float', x)
...         case Color(red, green, blue, name='red'):
...             print(type(subject).__name__, subject.name, red, green, blue)
...         case Color(red, green, 255) as color:
...             print(type(subject).__name__, color.name, red, green, color.blue)
...         case _: print(type(subject), subject)
...
float 42.0
Color red 255 0 0
Color anonymous 0 0 255
>>> match color_red:
...     case Color(red, green, blue, name):
...         print("matched")
...
Traceback (most recent call last):
  ...
TypeError: Color() accepts 3 positional sub-patterns (4 given)
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
