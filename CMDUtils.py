# coding=utf8
import sys, os
from functools import wraps
from OracleUtils import DBInstance
from LogWrapper import Logging4CLI

command_path = './command'


class CLIController(object):
    def __init__(self):
        self.controller = CMDPacket()
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


def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class CMDPacket(object):
    __db = None
    __cmds = None

    def __init__(self):
        self.__db = DBInstance(dump=True)
        self.__cmds = self.__loadObjects(command_path, self.__db)

    def hasCMD(self, cmd_name):
        if cmd_name in self.__cmds.keys():
            return True
        return False

    def execute(self, cmd_spl):
        """ execute command """
        cmd_name = cmd_spl[0]
        # parse command format
        args_dict = self.__cmds[cmd_name].parse(cmd_spl[1:])
        if args_dict is not None:
            self.__cmds[cmd_name].run(**args_dict)

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
            instant = C(self.__db)
            if hasattr(instant, 'cmd_name') and instant.cmd_name != 'base':
                # print 'load command %s.' % instant.cmd_name
                objs[instant.cmd_name] = instant
        return objs
