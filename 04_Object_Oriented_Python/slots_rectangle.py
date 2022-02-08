class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        '''area of the rectangle'''
        return self.width * self.height

class OptimizedRectangle(Rectangle):
    __slots__ = 'width', 'height'

# 3.8++
class OptimizedRectangle(Rectangle):
    __slots__ = {'width': 'rectangle width in pixels',
                 'height': 'rectangle height in pixels'}

# display docstrings with help()
help(OptimizedRectangle)


opt_r = OptimizedRectangle(100, 100)
print(vars(opt_r))  # <- prints empty dict, since __slots__ objects have no __dict__
print({name: getattr(opt_r, name) for name in opt_r.__slots__})
print(opt_r.area)