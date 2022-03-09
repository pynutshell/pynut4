import multiprocessing as mp
import os

def f(s):
    """Run a long time, and eventually return a result."""
    import time, random
    time.sleep(random.random()*2)  # simulate slowness
    return s+s  # some computation or other

def runner(s, d):
    print(os.getpid(), s)
    d[s] = f(s)

def make_dict(set_of_strings):
    mgr = mp.Manager()
    d = mgr.dict()
    workers = []
    for s in set_of_strings:
        p = mp.Process(target=runner, args=(s, d))
        p.start()
        workers.append(p)
    for p in workers:
        p.join()
    return {**d}

if __name__ == '__main__':
    dd = make_dict(list("ABCDE"))
    print(dd)
