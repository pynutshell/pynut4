import datetime
import random
import threading
import time


def runner():
    print('starting')
    time.sleep(random.randint(1, 3))
    print('waiting')
    if event is not None:
        event.wait()
    print(f'running at {datetime.datetime.now()}')


num_threads = 10
event = threading.Event()
# uncomment to see the behavior of threads without Event synchronization
# event = None

threads = [threading.Thread(target=runner) for _ in range(num_threads)]
for t in threads:
    t.start()

if event is not None:
    event.set()

for t in threads:
    t.join()
