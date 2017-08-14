# coding=utf8
from BaseAgent import baseAgent

class cdAgent(baseAgent):
    def __init__(self, db):
        super(cdAgent, self).__init__()
        self.db = db
        self.table = None

        self.parser.add_argument('table', type=str, help="cd target table name.")

    def parse(self, cmd_spl):
        try:
            args, unknown = self.parser.parse_known_args(cmd_spl)
            print args
            return vars(args)
        except Exception, ex:
            self.log_error(ex)

    def run(self, table):
        try:
            query_res = self.db.execute_sql('select count(*) from "%s"' % (table))
            self.dump_table([['Table', 'Rows'], [table, query_res[0][0]]])
            self.table = table
        except Exception, ex:
            self.log_error(ex)
