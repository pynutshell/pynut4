def safe_divide_1(x, y):
    if y==0:
        print('Divide-by-0 attempt detected')
        return None
    else:
        return x/y


def safe_divide_2(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        print('Divide-by-0 attempt detected')
        return None


for divisor in (10, 0):
    print(f'safe_divide_1(1, {divisor}) = {safe_divide_1(1, divisor)}')
    print(f'safe_divide_2(1, {divisor}) = {safe_divide_2(1, divisor)}')
