import queue
import threading
import time
from itertools import count


class Serializer(threading.Thread):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.daemon = True
        self.work_request_queue = queue.Queue()
        self.work_results = {}
        self.request_id_generator = count()
        self.start()

    def run(self):
        while True:
            seq_num, callable, args, kwds = self.work_request_queue.get(timeout=3)
            self.work_results[seq_num] = callable(*args, **kwds)

    def apply(self, callable, *args, **kwds):
        """called by other threads as `callable` would be"""
        request_seq_num = next(self.request_id_generator)
        self.work_request_queue.put((request_seq_num, callable, args, kwds))
        result_not_yet_available_sentinel = object()
        while True:
            result = self.work_results.pop(request_seq_num, result_not_yet_available_sentinel)
            if result is not result_not_yet_available_sentinel:
                return result
            time.sleep(0.05)


# ====== demo only - do not include in book copy ======

if __name__ == '__main__':

    """Tests the Serializer class."""
    serializer = Serializer()

    def request_fn(ii):
        expected = ii*ii
        actual = serializer.apply(lambda x: x * x, ii)
        if True:  # actual != expected:
            print(
                f"\n{expected=}, {actual=} {'<<<' if (expected != actual) else ''}",
                end="",
                flush=True
            )

    num_threads = 100
    for i in range(num_threads):
        thread = threading.Thread(target=request_fn, args=(i,))
        thread.start()
