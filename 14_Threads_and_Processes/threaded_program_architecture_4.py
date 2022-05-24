import random, time
import queue
# copy here class Worker as defined above
from threaded_program_architecture_3 import Worker

requests_queue = queue.Queue()
results_queue = queue.Queue()

number_of_workers = 3
workers = [Worker(requests_queue, results_queue)
           for i in range(number_of_workers)]
work_requests = {}

def pick_a_worker():
    return random.choice(workers)

def make_work():
    o1 = random.randrange(2, 10)
    o2 = random.randrange(2, 10)
    op = random.choice(('+', '-', '*', '/', '%', '**'))
    return f'{o1} {op} {o2}'

def slow_evaluate(expression_string):
    time.sleep(random.randrange(1, 5))
    return eval(expression_string)

def show_results():
    while True:
        try:
            id, results = results_queue.get_nowait()
        except queue.Empty:
            return
        print('Result {}: {} -> {}'.format(
            id, work_requests[id], results))
        del work_requests[id]

for i in range(10):
    expression_string = make_work()
    worker = pick_a_worker()
    id = worker.perform_work(slow_evaluate, expression_string)
    work_requests[id] = expression_string
    print(f'Submitted request {id}: {expression_string}')
    time.sleep(1.0)
    show_results()

while work_requests:
    time.sleep(1.0)
    show_results()
