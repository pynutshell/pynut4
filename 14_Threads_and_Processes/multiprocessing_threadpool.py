from multiprocessing.pool import ThreadPool

from multiprocessing_pool import runner


def make_dict(strings):
    d = {}
    with ThreadPool(3) as pool:
        for key, value in pool.imap_unordered(runner, strings):
            d[key] = value
    return d


if __name__ == '__main__':
    dd = make_dict(list("ABCDE"))
    print(dd)
