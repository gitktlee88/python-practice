import MySQLdb
# import logging
import os

class MySQLdb_connection(object):
    """mysql db connection"""
    def __init__(self, connection_string=os.environ["CONN"], db='mydic'):
        # connect(host, user, passwd, db)
        if db != 'mydic':
            connection_string = connection_string + ',' + db

        # connection_string = connection_string + ',' + 'charset=utf8mb4'

        vars = connection_string.split(',')
        self.host = vars[0]
        self.user = vars[1]
        self.pw = vars[2]
        self.char = "utf8mb4"

        self.connector = None

    ''' __enter()__ and __exit()__
    These  are  methods of the "context manager".
    and are known as "dunder methods", as they are surrounded
    by double underscores.
    Both the "enter()" and "exit()" methods are called every time
    the "with" statement is executed no matter how the code block
    terminates.
    So, basically a context manager ensures that resources are
    properly and automatically managed around the code that uses
    these resources.
    '''
    def __enter__(self):
        # self.connector = MySQLdb.connect(*self.connection_string)
        self.connector = MySQLdb.connect(host=self.host,
                                            user=self.user,
                                            passwd=self.pw,
                                            charset=self.char,)
        return self.connector

    def __exit__(self, exc_type, exc_val, exc_tb):
        # print('MySQLdb_connection.__exit__:'
        #             'Exception Detected\n'
        #             'type={}, value={}, traceback={}'.format(exc_type, exc_val, exc_tb))
        if exc_tb is None:
            self.connector.commit()
        else:
            self.connector.rollback()
        self.connector.close()


    """   fetchall(),
      the return value is a sequence of "tuples" that contain
      the "row values".
    """
    def query_db(self, sql_cmd, db_use = ''):
        with MySQLdb_connection(db = db_use) as conn:
            with conn.cursor() as cur:
                r = cur.execute(sql_cmd)
                #print(r)
                if r != 0:
                    r = cur.fetchall()
                return r


# executes when your script is called from the command-line
if __name__ == "__main__":
    print('How to use?\n'
          'MySQLdb_connection.query_db("your-sql-cmd")')

"""
    # sql = "INSERT INTO mydic.words (word, descr) VALUES ('%s', '%s')" % \
    # ('00test', 'test data description')
    # MySQLdb_connection.query_db(sql)
    #
    # sql = "SELECT word FROM mydic.words WHERE word = '00test'"
    # results = MySQLdb_connection.query_db(sql)
    # print(results)
    #
    # sql = "DELETE FROM mydic.words WHERE word = '00test'"
    # results = MySQLdb_connection.query_db(sql)
    # print(results)
    #
    # assert results[0][0] == 'first decorator'
"""
