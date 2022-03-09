import random, time

def make_work():
    o1 = random.randrange(2,10)
    o2 = random.randrange(2,10)
    op = random.choice(('+', '-', '*', '/', '%', '**'))
    return f'{o1} {op} {o2}'

def slow_evaluate(expression_string):
    time.sleep(random.randrange(1, 5))
    return eval(expression_string)

workRequests = {}
def showResults():
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
    id = worker.perform_work(slow_evaluate, expression_string)
    work_requests[id] = expression_string
    print(f'Submitted request {id}: {expression_string}')
    time.sleep(1.0)
    showResults()

while work_requests:
    time.sleep(1.0)
    showResults()
