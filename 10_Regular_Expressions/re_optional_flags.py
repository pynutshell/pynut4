import re


r1 = re.compile(r'(?i)hello')
r2 = re.compile(r'hello', re.I)
r3 = re.compile(r'hello', re.IGNORECASE)


repat_num1 = r'(0o[0-7]*|0x[\da-fA-F]+|[1-9]\d*)\Z'
repat_num2 = r'''(?x)            # (re.VERBOSE) pattern matching int literals
              (  0o [0-7]*       # octal: leading 0o, 0+ octal digits
               | 0x [\da-fA-F]+  # hex: 0x, then 1+ hex digits
               | [1-9] \d*       # decimal: leading non-0, 0+ digits
              )\Z                # end of string
              '''

