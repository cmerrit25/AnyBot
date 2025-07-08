import logging

logger = logging.getLogger(__name__)

def start_logger(logfile='logging.log', level=logging.INFO):
    logging.basicConfig(filename=logfile, level=level)