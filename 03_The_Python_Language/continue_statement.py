some_container = list(range(-10, 11))

def seems_ok(i):
    return i % 3

def bounds_to_test():
    return (-4, 4)

def pre_process(i):
    print(i, i * i)

def final_check(i):
    return i % 2

def do_processing(i):
    print(i, i * i * i)


for x in some_container:
    if seems_ok(x):
        lowbound, highbound = bounds_to_test()
        if lowbound <= x < highbound:
            pre_process(x)
            if final_check(x):
                do_processing(x)


# same for loop using continue
for x in some_container:
    if not seems_ok(x):
        continue

    lowbound, highbound = bounds_to_test()
    if x < lowbound or x >= highbound:
        continue

    pre_process(x)
    if final_check(x):
        do_processing(x)
