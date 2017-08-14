# coding=utf8
import logging

logger = logging.getLogger()
logger.setLevel(logging.WARNING)
console = logging.StreamHandler()
console.setFormatter(logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s"))
logger.addHandler(console)

class baseAgent(object):
    cmd_name = None
    def __init__(self, db=None):
        self.cmd_name = self.__class__.__name__.replace('Agent','')

    def run(self, args):
        pass

    def log(self, msg, log_type='info'):
        """ print log """
        to_print = getattr(logging, log_type, logging.info)
        to_print(msg)

    def dump_str(self, msg):
        """ output result message """
        print('[Result] %s', msg)

    def dump_table(self, arr):
        pass


# logging.info('222')
# x = CMDBase()
# x.log('111', log_type='warning')
