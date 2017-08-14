# coding=utf8
import cx_Oracle
import json
import os

with open('config.json') as config_file:
    config = json.load(config_file)

# default configuation
os.environ['NLS_LANG'] = config['NLS_LANG']

default_user = config['DataBase']['user']
default_pass = config['DataBase']['pass']
default_dsn = cx_Oracle.makedsn(config['DataBase']['host'],
                                config['DataBase']['port'],
                                config['DataBase']['dbn'])

class DBInstance(object):
    def __init__(self, user=default_user, passwd=default_pass, dsn=default_dsn, dump=False):
        self.db_connect = cx_Oracle.connect(user, passwd, dsn)
        self.cursor = self.db_connect.cursor()
        self.dump = dump

    def execute_sql(self, sql_str):
        if self.dump:
            print (sql_str)
        try:
            query_res = self.cursor.execute(sql_str)
            return query_res.fetchall()
        except Exception, ex:
            raise Exception(ex)
