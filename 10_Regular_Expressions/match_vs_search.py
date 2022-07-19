import re

r1 = re.compile(r'box')
if r1.match('inbox'):
    print('match succeeds')
else:
    print('match fails')  # prints: match fails

if r1.search('inbox'):
    print('search succeeds')  # prints: search succeeds
else:
    print('search fails')
