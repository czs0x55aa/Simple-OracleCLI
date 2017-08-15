# coding=utf8
from BaseAgent import baseAgent

class lsAgent(baseAgent):
    def __init__(self, db):
        super(lsAgent, self).__init__()
        self.db = db

        self.parser.add_argument('table', type=str, nargs='?', default='.', help="target table name.")

    def parse(self, cmd_spl):
        try:
            args, unknown = self.parser.parse_known_args(cmd_spl)
            return vars(args)
        except Exception, ex:
            self.log_error(ex)

    def run(self, table):
        try:
            # if table == '.':
            #     table = self.bin['cd'].table
            query_res = self.db.execute_sql('select * from "%s"' % table)
            self.dump_table(query_res)
        except Exception, ex:
            self.log_error(ex)
