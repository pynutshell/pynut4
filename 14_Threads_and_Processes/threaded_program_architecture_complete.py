import random, time, queue, operator
# copy here class Worker as defined above
from threaded_program_architecture_worker import Worker

requests_queue = queue.Queue()
results_queue = queue.Queue()

number_of_workers = 3
workers = [Worker(requests_queue, results_queue)
           for i in range(number_of_workers)]
work_requests = {}

operations = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
    '%': operator.mod,
}

def pick_a_worker():
    return random.choice(workers)

def make_work():
    o1 = random.randrange(2, 10)
    o2 = random.randrange(2, 10)
    op = random.choice(list(operations))
    return f'{o1} {op} {o2}'

def slow_evaluate(expression_string):
    time.sleep(random.randrange(1, 5))
    op1, oper, op2 = expression_string.split()
    arith_function = operations[oper]
    return arith_function(int(op1), int(op2))

def show_results():
    while True:
        try:
            completed_id, results = results_queue.get_nowait()
        except queue.Empty:
            return
        work_expression = work_requests.pop(completed_id)
        print(f'Result {completed_id}: {work_expression} -> {results}')


for i in range(10):
    expression_string = make_work()
    worker = pick_a_worker()
    request_id = worker.perform_work(slow_evaluate, expression_string)
    work_requests[request_id] = expression_string
    print(f'Submitted request {request_id}: {expression_string}')
    time.sleep(1.0)
    show_results()

while work_requests:
    time.sleep(1.0)
    show_results()
