# coding=utf8
import sys, os

from OracleUtils import DBInstance
from LogWrapper import Logging4CLI
from Toolkit import singleton

command_path = './command'


class CLIController(object):
    def __init__(self):
        self.controller = CMDManager()
        self.logging = Logging4CLI()

    def resolve(self, cmd):
        cmd_spl = cmd.split()
        if len(cmd_spl) == 0:
            return
        cmd_name = cmd_spl[0]
        if self.controller.hasCMD(cmd_name):
            self.controller.execute(cmd_spl)
        else:
            self.logging.error('Command not exist.')


class CMDManager(object):
    def __init__(self):
        self.db = DBInstance(dump=True)
        self.bin = BINPacket(self.db)

    def hasCMD(self, cmd_name):
        if cmd_name in self.bin.get_keys():
            return True
        return False

    def execute(self, cmd_spl):
        """ execute command """
        cmd_name = cmd_spl[0]
        # parse command format
        args_dict = self.bin[cmd_name].parse(cmd_spl[1:])
        if args_dict is not None:
            self.bin[cmd_name].run(**args_dict)


@singleton
class BINPacket(object):
    __cmds = None

    def __init__(self, db=None):
        self.__cmds = self.__loadObjects(command_path, db)

    def __getitem__(self, key):
        return self.__cmds[key]

    def get_keys(self):
        return self.__cmds.keys()

    def __loadObjects(self, path, db):
        sys.path.append(path)
        modules = []
        # search and import module in directory
        for root, dirs, files in os.walk(path):
            for fname in files:
                mod_name, suffix = os.path.splitext(fname)
                if suffix == '.py':
                    modules.append(__import__(mod_name))

        clas = set()
        for modl in modules:
            for attr in dir(modl):
                item = getattr(modl, attr)
                # store object named xxxAgent
                if type(item) == type(object) and item.__name__.find('Agent') > 0:
                    clas.add(item)
        # load objects
        objs = {}
        for C in clas:
            instant = C(db)
            if hasattr(instant, 'cmd_name') and instant.cmd_name != 'base':
                # print 'load command %s.' % instant.cmd_name
                objs[instant.cmd_name] = instant
        return objs
