import threading

class Periodic(threading.Timer):
    def __init__(self, interval, callback, args=None, kwargs=None):
        super().__init__(interval, self._f, args, kwargs)
        self.callback = callback

    def _f(self, *args, **kwargs):
        p = type(self)(self.interval, self.callback, args, kwargs)
        p.start()
        try:
            self.callback(*args, **kwargs)
        except Exception:
            p.cancel()


def countdown():
    global times
    times -= 1
    if times < 0:
        raise Exception('all done!')
    print('...', times, sep='', end='')


times = 11
Periodic(1, countdown).start()
