# coding=utf8
from BaseAgent import baseAgent

class unlimitedAgent(baseAgent):
    def __init__(self, db):
        super(unlimitedAgent, self).__init__()
        self.db = db
        self.cmd_name = ':'

    def parse(self, cmd_spl):
        return {'sql': ' '.join(cmd_spl)}

    def run(self, sql):
        try:
            query_res = self.db.execute_sql(sql)
            print (query_res)
            self.dump_table(query_res)
        except Exception, ex:
            self.log_error(ex)
