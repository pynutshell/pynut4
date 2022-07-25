"""
>>> s = 'a string'
>>> '{0:>{1}s}'.format(s, len(s)+4)
'    a string'
>>> '{0:_^{1}s}'.format(s, len(s)+4)
'__a string__'

>>> def columnar_strings(str_seq, widths):
...     for cols in str_seq:
...         row = ['{c:{w}.{w}s}'.format(c=c, w=w)
...                 for c, w in zip(cols, widths)]
...         print(' '.join(row))

>>> c = [
...      'four score and'.split(),
...      'seven years ago'.split(),
...      'our forefathers brought'.split(),
...      'forth on this'.split(),
...  ]

>>> columnar_strings(c, (8, 8, 8))
four     score    and     
seven    years    ago     
our      forefath brought 
forth    on       this    
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
