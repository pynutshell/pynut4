import queue

q = queue.Queue()

if q.empty():
    print('no work to perform')
else:
    x = q.get_nowait()
    work_on(x)
