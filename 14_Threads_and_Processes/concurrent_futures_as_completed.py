import concurrent.futures as cf

from concurrent_futures import runner

def make_dict(strings):
    with cf.ProcessPoolExecutor() as e:
        futures = [e.submit(runner, s) for s in strings]
        d = dict(f.result()
                 for f in cf.as_completed(futures))
    return d

if __name__ == '__main__':
    dd = make_dict(list("ABCDE"))
    print(dd)
