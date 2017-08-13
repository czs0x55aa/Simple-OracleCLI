# coding=utf8
import logging

logger = logging.getLogger()
logger.setLevel(logging.WARNING)
console = logging.StreamHandler()
console.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"))
logger.addHandler(console)

class CMDBase(object):
    def __init__(self, db):
        self.db = db
        pass

    def run(self, args):
        pass

    def log(self, msg, log_type='info'):
        """ print log """
        to_print = getattr(logging, log_type, logging.info)
        to_print(msg)

    def dump(self, msg):
        """ output result message """
        print('[Result] %s', msg)


# logging.info('222')
# x = CMDBase()
# x.log('111', log_type='warning')
