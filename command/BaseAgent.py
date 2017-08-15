# coding=utf8
from terminaltables import AsciiTable

from CMDUtils import BINPacket
from LogWrapper import Logging4CLI
from Toolkit import ThrowingArgumentParser

class baseAgent(object):
    cmd_name = None
    def __init__(self, db=None):
        self.cmd_name = self.__class__.__name__.replace('Agent','')
        self.parser = ThrowingArgumentParser()
        self.logging = Logging4CLI()
        # self.bin = BINPacket()

    def parse(self, arg_list):
        return None

    def run(self, args):
        pass

    def log_info(self, msg):
        self.logging.info('[%s]: %s' % (self.cmd_name, msg))

    def log_warning(self, msg):
        self.logging.warning('[%s]: %s' % (self.cmd_name, msg))

    def log_error(self, msg):
        self.logging.error('[%s]: %s' % (self.cmd_name, msg))

    def dump_str(self, msg):
        """ output message """
        print('[Result] %s', msg)

    def dump_table(self, table_data):
        """ output table """
        table = AsciiTable(table_data)
        print table.table


# logging.info('222')
# x = CMDBase()
# x.log('111', log_type='warning')
