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
            sql_split = sql.split()
            if sql_split.index('*') >= 0 and sql_split.index('from') >= 0:
                table_name = sql_split[sql_split.index('from') + 1].split('"')[1]
                struct_sql = "select column_name from user_tab_columns where table_name='%s'" % table_name
                table_head = self.db.execute_sql(struct_sql)
                table_head = [x[0] for x in table_head]
            self.dump_table([table_head] + query_res)
        except Exception, ex:
            self.log_error(ex)
