# common setup steps
import logging
logging.basicConfig(
    format='%(asctime)s %(levelname)8s %(message)s',
    filename='/tmp/logfile.txt', filemode='w')


logging.getLogger().setLevel(logging.DEBUG)
logging.getLogger().setLevel(logging.ERROR)
