import re
first_last = re.compile(r'^\W*(\w+)\b.*\b(\w+)\W*$',re.MULTILINE)
with open('afile.txt') as f:
    for first, last in first_last.findall(f.read()):
       print(first, last)
