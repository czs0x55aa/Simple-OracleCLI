# coding=utf8
import json
import os

from LogWrapper import Logging4CLI

with open('config.json') as config_file:
    config = json.load(config_file)

# default configuation
os.environ['NLS_LANG'] = config['NLS_LANG']
import cx_Oracle

default_user = config['DataBase']['user']
default_pass = config['DataBase']['pass']
default_dsn = cx_Oracle.makedsn(config['DataBase']['host'],
                                config['DataBase']['port'],
                                config['DataBase']['dbn'])

welcome_str = """
 _    _      _
| |  | |    | |
| |  | | ___| | ___ ___  _ __ ___   ___
| |/\| |/ _ \ |/ __/ _ \| '_ ` _ \ / _ \\
\  /\  /  __/ | (_| (_) | | | | | |  __/
 \/  \/ \___|_|\___\___/|_| |_| |_|\___|
"""

class DBInstance(object):
    def __init__(self, user=default_user, passwd=default_pass, dsn=default_dsn, dump=False):
        self.logging = Logging4CLI()
        self.db_connect = cx_Oracle.connect(user, passwd, dsn)
        self.cursor = self.db_connect.cursor()
        self.dump = dump

        print (welcome_str)
        self.logging.info('Connect OK.')

    def execute_sql(self, sql_str):
        if self.dump:
            self.logging.info('[SQL]: %s' % sql_str)
        try:
            query_res = self.cursor.execute(sql_str)
            return query_res.fetchall()
        except Exception, ex:
            raise Exception(ex)
