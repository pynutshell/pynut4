import sys
g = sys.modules[__name__]
v1 = "one"; v2 = 2; v3 = 2.56
match ('one', 2, 2.56):
    case (g.v1, g.v2, g.v3):  print('matched')

# prints 'matched'
