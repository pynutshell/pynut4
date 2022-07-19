{'x':42, 'y':3.14, 'z':7}    # Dictionary with three items, str keys
{1:2, 3:4}                   # Dictionary with two items, int keys
{1:'za', 'br':23}            # Dictionary with different key types
{}                           # Empty dictionary

dict(x=42, y=3.14, z=7)      # Dictionary with three items, str keys
dict([(1, 2), (3, 4)])       # Dictionary with two items, int keys
dict([(1,'za'), ('br',23)])  # Dictionary with different key types
dict()                       # Empty dictionary

dict.fromkeys('hello', 2)   # same as {'h':2, 'e':2, 'l':2, 'o':2}
dict.fromkeys([1, 2, 3])    # same as {1:None, 2:None, 3:None}
