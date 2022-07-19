ba = bytearray([97, 98, 99]) # like bytes, can construct from a sequence of ints
ba[1] = 97                   # unlike bytes, contents can be modified
print(ba.decode())           # prints 'aac'
