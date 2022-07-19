d = {'x':42, 'y':3.14, 'z':7}
d['x']                           # 42
d['z']                           # 7
d['a']                           # raises KeyError exception

d = {'x':42, 'y':3.14}
d['a'] = 16                    # d is now {'x':42, 'y':3.14, 'a':16}

