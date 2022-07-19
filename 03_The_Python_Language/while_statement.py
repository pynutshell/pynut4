"""
while expression:
    statement(s)
"""

count = 0
x = 99
while x > 0:
    x //= 2            # floor division
    count += 1
print('The approximate log2 is', count)
