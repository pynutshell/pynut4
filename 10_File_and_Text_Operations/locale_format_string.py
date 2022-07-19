"""
>>> import locale

>>> locale.setlocale(locale.LC_NUMERIC, 'en_us')
'en_us'
>>> n=1000*1000
>>> locale.format_string('%d', n)
'1000000'
>>> locale.setlocale(locale.LC_MONETARY, 'it_it')
'it_it'
>>> locale.format_string('%f', n)
'1000000.000000' #uses decimal_point
>>> locale.format_string('%f', n, monetary=True)
'1000000,000000' #uses mon_decimal_point
>>> locale.format_string('%0.2f', n, grouping=True)
'1,000,000.00' # separators & decimal from LC_NUMERIC
>>> locale.format_string('%0.2f', n, grouping=True, monetary=True)
'1.000.000,00' # separators & decimal from LC_MONETARY
"""