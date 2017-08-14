# coding=utf8
import sys, os
from functools import wraps
from OracleUtils import DBInstance


command_path = './command'

class Parser(object):
    def __init__(self):
        self.cmdManager = CMDManager()

    def resolve(self, cmd):
        def operate(args):
            pass
        cmd_spl = cmd.split()
        if len(cmd_spl) == 0:
            return {}, ''
        cmd_head = cmd_spl[0]
        operate_func = self.cmdManager.getOperat(cmd_head)
        if cmd_head == 'exit':
            operate_func()
        elif cmd_head == 'cd' and len(cmd_spl) >= 2:
            operate_func(t=cmd_spl[1])

def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance

@singleton
class CMDManager(object):
    __db = None
    __cmds = None

    def __init__(self):
        self.__db = DBInstance(dump=True)
        self.__cmds = self.__loadObjects(command_path, self.__db)

    def getOperat(self, cmd_name):
        if cmd_name in self.__cmds.keys():
            return self.__cmds[cmd_name].run
        return None

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
                # print part, type(item)
                if type(item) == type(object):
                    clas.add(item)
        # load objects
        objs = {}
        for C in clas:
            instant = C(db)
            if instant.cmd_name != 'base':
                objs[instant.cmd_name] = instant
        return objs
