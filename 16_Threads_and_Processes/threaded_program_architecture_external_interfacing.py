import threading, queue


class ExternalInterfacing(threading.Thread):
    def __init__(self, external_callable, **kwds):
        super().__init__(**kwds)
        self.daemon = True
        self.external_callable = external_callable
        self.request_queue = queue.Queue()
        self.result_queue = queue.Queue()
        self.start()

    def request(self, *args, **kwds):
        """called by other threads as external_callable would be"""
        self.request_queue.put((args, kwds))
        return self.result_queue.get()

    def run(self):
        while True:
            a, k = self.request_queue.get()
            self.result_queue.put(self.external_callable(*a, **k))

