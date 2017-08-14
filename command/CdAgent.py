# coding=utf8
from BaseAgent import baseAgent

class cdAgent(baseAgent):
    def __init__(self, db):
        super(cdAgent, self).__init__()
        self.db = db
        self.table = None

    def run(self, t=None):
        if t is not None:
            try:
                query_res = self.db.execute_sql('select count(*) from "%s"' % (t))
                if query_res is not None:
                    print query_res
                # print 'table %s rows: %d.' % (table_name, res[0][0])
                self.table = t
            except Exception, ex:
                print Exception, ex
        else:
            self.log('table name required.', log_type='warning')
