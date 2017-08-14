# coding=utf8
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
