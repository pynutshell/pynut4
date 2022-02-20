import pdb

def f(x):
    pdb.set_trace()
    # At (Pdb) prompt, 'x' will display the value for x

    # Enter 'c' command to advance to the next breakpoint
    if x > 100:
        q = x**2
    else:
        q = x

    pdb.set_trace()
    # At (Pdb) prompt, 'q' will *not* display the value for q
    # since 'q' is defined as an abbreviation for the Pdb 'quit'
    # command - exiting the debugger and the program!
    #
    # To view the value for q, enter '!q' or `p q`.
    return q

f(10)
