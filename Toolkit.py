# coding=utf8
from functools import wraps
import argparse

class ArgumentParserError(Exception):
    pass

class ThrowingArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        raise ArgumentParserError(message)

def catch_exception(func):
    def wrapper(*args, **kw):
        try:
            return func(*args, **kw)
        except Exception, ex:
            print ex
    return wrapper


def singleton(cls):
    instances = {}
    @wraps(cls)
    def getinstance(*args, **kw):
        if cls not in instances:
            instances[cls] = cls(*args, **kw)
        return instances[cls]
    return getinstance
