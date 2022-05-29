import concurrent.futures as cf

from concurrent_futures import runner

def make_dict(strings):
    with cf.ProcessPoolExecutor() as e:
        d = dict(f.result()
                 for f in cf.as_completed(
                    e.submit(runner, s) for s in strings))
    return d

if __name__ == '__main__':
    dd = make_dict(list("ABCDE"))
    print(dd)
