import datetime
import random
import threading
import time


def runner():
    print('starting')
    time.sleep(random.randint(1, 3))
    print('waiting')
    if barrier is not None:
        try:
            my_number = barrier.wait()
        except threading.BrokenBarrierError:
            print('Barrier abort() or reset() called, thread exiting...')
            return
        print(f'running ({my_number}) at {datetime.datetime.now()}')
    else:
        print(f'running at {datetime.datetime.now()}')


def announce_release():
    print('releasing')


num_threads = 10
barrier = threading.Barrier(num_threads, action=announce_release)
# uncomment to see the behavior of threads without Barrier synchronization
# barrier = None

threads = [threading.Thread(target=runner) for _ in range(num_threads)]
for t in threads:
    t.start()

for t in threads:
    t.join()
