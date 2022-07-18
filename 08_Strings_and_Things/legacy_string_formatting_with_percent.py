import logging

logging.getLogger().setLevel(logging.INFO)
x = 42
y = 3.14
z = 'george'

logging.info('result = %d', x)        # logs: result = 42
logging.info('answers: %d %f', x, y)  # logs: answers: 42 3.140000
logging.info('hello %s', z)           # logs: hello george
