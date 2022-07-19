import threading

class Worker(threading.Thread):
    IDlock = threading.Lock()
    request_ID = 0

    def __init__(self, requests_queue, results_queue, **kwds):
        super().__init__(**kwds)
        self.daemon = True
        self.request_queue = requests_queue
        self.result_queue = results_queue
        self.start()

    def perform_work(self, callable, *args, **kwds):
        """called by main thread as `callable` would be, but w/o return"""
        with self.IDlock:
            Worker.request_ID += 1
            self.request_queue.put(
                (Worker.request_ID, callable, args, kwds))
            return Worker.request_ID

    def run(self):
        while True:
            request_ID, callable, a, k = self.request_queue.get()
            self.result_queue.put((request_ID, callable(*a, **k)))


if __name__ == '__main__':
    import queue

    requests_queue = queue.Queue()
    results_queue = queue.Queue()
    number_of_workers = 5
    for i in range(number_of_workers):
        worker = Worker(requests_queue, results_queue)
