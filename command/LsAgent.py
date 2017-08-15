# coding=utf8
from BaseAgent import baseAgent

class lsAgent(baseAgent):
    def __init__(self, db):
        super(lsAgent, self).__init__()
        self.db = db

        self.parser.add_argument('-t', '-table', type=str, help="target table name.")

    def parse(self, cmd_spl):
        try:
            args, unknown = self.parser.parse_known_args(cmd_spl)
            print args
            return vars(args)
        except Exception, ex:
            self.log_error(ex)

    def run(self, table):
        try:
            if table is None:
                query_res = self.db.execute_sql('select table_name from user_tables')
            else:
                query_res = self.db.execute_sql('select * from "%s"' % table)
            self.dump_table(query_res)
        except Exception, ex:
            self.log_error(ex)
