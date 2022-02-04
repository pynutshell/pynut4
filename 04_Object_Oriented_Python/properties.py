import math

class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
    area = property(get_area, doc='area of the rectangle')

r = Rectangle(100, 100)
print(vars(r))
print(r.area)  # <- property, no ()'s

# property decorator
class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        '''area of the rectangle'''
        return self.width * self.height

r = Rectangle(200, 200)
print(vars(r))
print(r.area)


class Rectangle(object):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    @property
    def area(self):
        '''area of the rectangle'''
        return self.width * self.height
    @area.setter
    def area(self, value):
        scale = math.sqrt(value/self.area)
        self.width *= scale
        self.height *= scale

r = Rectangle(300, 300)
print(vars(r))
print(r.area)  # <- property, no ()'s
r.area = 10000
print(r.area)
print(vars(r))
