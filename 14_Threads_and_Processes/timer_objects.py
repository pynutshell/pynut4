import threading

class Periodic(threading.Timer):
    def __init__(self, interval, callable_fn, args=(), kwargs={}):
        super().__init__(interval, self._f, args, kwargs)
        self.callable = callable_fn

    def _f(self, *args, **kwargs):
        p = type(self)(self.interval, self.callable, args, kwargs)
        p.start()
        try:
            self.callable(*args, **kwargs)
        except Exception:
            p.cancel()


def countdown():
    global times
    times -= 1
    if times < 0:
        raise Exception("all done!")
    print("...", times, sep="", end="")


times = 11
Periodic(1, countdown).start()
