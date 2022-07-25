"""
>>> n = 10; s = 'zero', 'one', 'two', 'three'; i=2
>>> f'start {"-"*n} : {s[i]} end'
'start ---------- : two end'

>>> "This is a {0}, {1}, type of {type}".format("large", "green", type="vase")
'This is a large, green, type of vase'
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod()
