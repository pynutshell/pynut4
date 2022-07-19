import ast
print(ast.literal_eval('23'))     # prints 23
print(ast.literal_eval('  23'))   # prints 23 (||3.10++||)
print(ast.literal_eval('[2,-3]')) # prints [2, -3]
print(ast.literal_eval('2+3'))    # raises ValueError
print(ast.literal_eval('2+'))     # raises SyntaxError

