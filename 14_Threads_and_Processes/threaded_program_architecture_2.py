import threading, queue


class Serializer(threading.Thread):
    def __init__(self, **kwds):
        super().__init__(**kwds)
        self.daemon = True
        self.work_request_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self.start()

    def apply(self, callable, *args, **kwds):
        """called by other threads as `callable` would be"""
        self.work_request_queue.put((callable, args, kwds))
        return self.result_queue.get()

    def run(self):
        while True:
            callable, args, kwds = self.work_request_queue.get()
            self.result_queue.put(callable(*args, **kwds))
