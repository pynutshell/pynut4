import multiprocessing as mp

def make_list():
    some_manager = mp.Manager()
    p = some_manager.list()
    p[:] = [1, 2, 3]
    print(p == [1, 2, 3])  # prints False, as it compares with p itself
    print(list(p) == [1, 2, 3])  # prints True, as it compares with copy

    # this raises an Exception, because functions are not picklable
    p.append(lambda: None)


if __name__ == '__main__':
    make_list()
