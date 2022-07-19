# using try/finally
f = open(some_file, 'w')
try:
    do_something_with_file(f)
finally:
    f.close()


# using 'with' statement, with file object as a context manager
# (this is the preferred form for new Python code)
with open(some_file, 'w') as f:
    do_something_with_file(f)
