"""
>>> import locale

>>> locale.setlocale(locale.LC_NUMERIC, 'en_us')
'en_us'
>>> n=1000*1000
>>> locale.format_string('%d', n)
'1000000'
>>> locale.setlocale(locale.LC_MONETARY, 'it_it')
'it_it'
>>> locale.format_string('%f', n)  # uses decimal_point
'1000000.000000'
>>> locale.format_string('%f', n, monetary=True)  # uses mon_decimal_point
'1000000,000000'
>>> locale.format_string('%0.2f', n, grouping=True)  # separators & decimal from LC_NUMERIC
'1,000,000.00'
>>> locale.format_string('%0.2f', n, grouping=True, monetary=True)  # separators & decimal from LC_MONETARY
'1.000.000,00'
"""

if __name__ == '__main__':
    # use doctest to simulate console sessions
    import doctest
    doctest.testmod(verbose=True, exclude_empty=True)
