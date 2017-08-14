# coding=utf8
from BaseAgent import baseAgent

class exitAgent(baseAgent):
    def __init__(self, db):
        super(exitAgent, self).__init__()
        self.db = db

    def parse(self, arg_list):
        return {}

    def run(self):
        print ('Exit.')
        exit()
