import multiprocessing

a = multiprocessing.Array('c', b'four score and seven')
a.value = b'five'
print(a.value)
print(a[:])
