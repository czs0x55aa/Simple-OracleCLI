# coding=utf8
import sys, os

command_path = './command'

class Parser(object):
    def __init__(self):
        pass

    def resolve(self, cmd):
        cmd_spl = cmd.split()
        if len(cmd_spl) == 0:
            return {}, ''
        cmd_head = cmd_spl[0]
        if cmd_head == 'exit':
            return None, 'Exit.'
        elif cmd_head == 'cd' and len(cmd_spl) >= 2:
            return {'obj': 'cd', 'args': {'t': cmd_spl[1]}}, ''
        return {}, None

class Executor(object):
    def __init__(self, db):
        self.db = db
        self.objs = loadObjects(command_path, db)

    def execute(self, exe_config):
        if 'obj' in exe_config and 'args' in exe_config:
            obj_name = exe_config['obj']
            self.objs[obj_name].run(**exe_config['args'])


def loadObjects(path, db):
    sys.path.append(path)

    modules = []
    # search module in directory
    for root, dirs, files in os.walk(path):
        for fname in files:
            mod_name, suffix = os.path.splitext(fname)
            if suffix == '.py':
                modules.append(__import__(mod_name))

    clas = set()
    for mod in modules:
        for part in dir(mod):
            item = getattr(mod, part)
            # print part, type(item)
            if type(item) == type(object):
                clas.add(item)

    objs = {}
    for C in clas:
        objs[C.__name__.replace('CMD','')] = C(db)
        # print c, c.__name__
    return objs


# loadObjects(command_path)
