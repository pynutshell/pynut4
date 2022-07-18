# abs takes a numeric argument; let's make it accept a string as well
import builtins
_abs = builtins.abs                          # save original built-in

def abs(str_or_num):
    if isinstance(str_or_num, str):          # if arg is a string
        return ''.join(sorted(set(str_or_num)))  # get this instead
    return _abs(str_or_num)                  # call real built-in

builtins.abs = abs                    # override built-in w/wrapper


# conventional abs
print(abs(-100))

# special handling of abs(str)
print(abs("Bubble, bubble, toil and trouble"))
