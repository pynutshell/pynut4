import re
print(re.findall(r'\w+', 'cittá'))# prints ['cittá']
print(re.findall(rb'\w+', 'cittá'.encode())) # prints [b'citt']
