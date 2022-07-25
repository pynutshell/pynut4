"""
This module supplies a single function reverse_words that reverses
a string by words.

>>> reverse_words('four score and seven years')
'years seven and score four'
>>> reverse_words('justoneword')
'justoneword'
>>> reverse_words('')
''

You must call reverse_words with one argument, a string:

>>> reverse_words()
Traceback (most recent call last):
    ...
TypeError: reverse_words() missing 1 required positional argument: 'astring'
>>> reverse_words('one', 'another')
Traceback (most recent call last):
    ...
TypeError: reverse_words() takes 1 positional argument but 2 were given
>>> reverse_words(1)
Traceback (most recent call last):
    ...
AttributeError: 'int' object has no attribute 'split'
>>> reverse_words('𝒰𝓷𝓲𝓬𝓸𝓭𝓮 is all right too')
'too right all is 𝒰𝓷𝓲𝓬𝓸𝓭𝓮'

As a side effect, reverse_words eliminates any redundant spacing:

>>> reverse_words('with  redundant   spacing')
'spacing redundant with'

"""


def reverse_words(astring):
    words = astring.split()
    words.reverse()
    return ' '.join(words)


if __name__ == '__main__':
    import doctest

    doctest.testmod(verbose=True, exclude_empty=True)
