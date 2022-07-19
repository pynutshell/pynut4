def read_or_default(filepath, default):
    try:
        with open(filepath) as f:
            return f.read()
    except FileNotFoundError:
        return default

# read and output contents of this source file
for filename in (__file__, __file__ + 'y'):
    print(filename)
    print('-' * 40)
    print(read_or_default(filename, "<no file found>"))
    print('-' * 40)
