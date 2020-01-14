
import MySQLdb
import logging
import os
import pandas as pd

## //////// class version ///////////
class MySQLdb_connection(object):
    """mysql db connection"""
    def __init__(self, connection_string=os.environ["CONN"]):
        self.connection_string = connection_string.split(',')
        self.connector = None
    def __enter__(self):
        self.connector = MySQLdb.connect(*self.connection_string)
        return self.connector
    def __exit__(self, exc_type, exc_val, exc_tb):
        #print(exc_type, exc_val, exc_tb)
        if exc_tb is None:
            self.connector.commit()
        else:
            self.connector.rollback()
        self.connector.close()


## //////// decorator version ///////////

## A decorator is a design pattern in Python that allows
## a user to add new functionality to an existing object
## without modifying its structure.

# Python allows a nested function to access the outer scope of
# the enclosing function.
# This is a critical concept in decorators -- this pattern is
# known as a Closure.

def db_connector(func):
    def with_connection_(*args, **kwargs):
        #print(args, kwargs)
        conn_str = os.environ["CONN"]
        #print(conn_str)
        #conn_str = conn_str + ',' + 'mydic'  # default db
        cnn = MySQLdb.connect(*conn_str.split(','))
        try:
            rv = func(cnn, *args, **kwargs)
            #print(cnn, args, kwargs)
        except Exception:
            cnn.rollback()
            logging.error("Database connection error")
            raise
        else:
            cnn.commit()
        finally:
            cnn.close()
        return rv
    return with_connection_


@db_connector
def do_some_job(cnn, arg1, db_name=None):
    #print(cnn, arg1, db_name)
    cur = cnn.cursor()
    SQL = "SELECT descr FROM mydic.words WHERE word = '%s' " % (arg1)
    #cur.execute(SQL, (arg1, arg2)) # or something else
    cur.execute(SQL)
    print(cur.fetchall())

# executes when your script is called from the command-line
if __name__ == "__main__":
    #main(sys.argv)

    #### using decorator version
    # do_some_job('11test', db_name='mydic')   is   samme as
    # db_connector( do_some_job('11test', db_name='mydic') )
    do_some_job('11test', db_name='mydic')

    #### using class version
    sql = "SELECT * FROM mydic.words WHERE word = '11test' "
    with MySQLdb_connection() as conn:
        data =  pd.read_sql(sql, conn)
        #raise Exception('my exception test simulation')
    print(data)
