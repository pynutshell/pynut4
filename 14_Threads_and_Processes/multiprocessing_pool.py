import multiprocessing as mp
import os

def f(s):
    """Run a long time, and eventually return a result."""
    import time, random
    time.sleep(random.random()*2)  # simulate slowness
    return s+s  # some computation or other

def runner(s):
    print(os.getpid(), s)
    return s, f(s)

def make_dict(strings):
    with mp.Pool() as pool:
        d = dict(pool.imap_unordered(runner, strings))
        return d

if __name__ == '__main__':
    dd = make_dict(['A', 'B', 'C', 'D', 'E'])
    print(dd)
