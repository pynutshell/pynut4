# common setup steps
import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)8s %(message)s',
    filename='/tmp/logfile.txt', filemode='w')


logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger().setLevel(logging.ERROR)


def cpu_intensive_function():
    return 2**100

if logging.getLogger().isEnabledFor(logging.DEBUG):
    foo = cpu_intensive_function()
    logging.debug('foo is %r', foo)
