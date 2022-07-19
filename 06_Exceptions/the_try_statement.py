try:
    1/0
    print('not executed')
except ZeroDivisionError:
    print('caught divide-by-0 attempt')


try:
    try:
        1/0
    except:
        print('caught an exception')
except ZeroDivisionError:
    print('caught divide-by-0 attempt')


value = 'ABC'
print(repr(value), 'is ', end=' ')
try:
    value + 0
except TypeError:
    # not a number, maybe a string...?
    try:
        value + ''
    except TypeError:
        print('neither a number nor a string')
    else:
        print('some kind of string')
else:
    print('some kind of number')
