# coding=utf8
import logging
import colorlog

logger = colorlog.getLogger()
logger.setLevel(logging.INFO)
console = colorlog.StreamHandler()
console.setFormatter(colorlog.ColoredFormatter("%(log_color)s%(levelname)s - %(message)s"))
logger.addHandler(console)

class Logging4CLI(object):
    def __init__(self):
        pass

    def dump(self, msg, log_type='info'):
        print_log = getattr(logging, log_type, logging.info)
        print_log(msg)

    def info(self, msg):
        logging.info(msg)

    def warning(self, msg):
        logging.warning(msg)

    def error(self, msg):
        logging.error(msg)
