import merge
x = {'a':1,'b':2 }
merge.merge(x,[['b',3],['c',4]])
print(x)                           # prints: {'a':1, 'b':2, 'c':4 }
print(merge.mergenew(x,{'a':5,'d':6},override=1)) # prints: {'a':5, 'b':2, 'c':4, 'd':6 }
print(x)                           # prints: {'a':1, 'b':2, 'c':4 }
