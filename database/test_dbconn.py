import os
import dbconn as db
import MySQLdb
import unittest
import datetime as dt

### python -m unittest test_db.py

class TestMySQLdb_connection(unittest.TestCase):
    """
    Test the MySQLdb_connection
    """
    def setUp(self):
        """
        Setup here,    create database & create table
        """
        print('setUp...')
        # db.MySQLdb_connection.create_db(db_name = 'mydb')
        sql = "CREATE DATABASE IF NOT EXISTS %s" % 'mydb'
        # db.MySQLdb_connection.query_db(sql, db_use = 'mydic')
        db.MySQLdb_connection.query_db(sql)

        sql = "CREATE TABLE IF NOT EXISTS %s (id INT AUTO_INCREMENT \
            PRIMARY KEY, name VARCHAR(255), salary INT(6))" % 'test'
        r2 = db.MySQLdb_connection.query_db(sql, db_use = 'mydb')
        #print(r2)
        r2 = db.MySQLdb_connection.query_db("SHOW TABLES;", db_use = 'mydb')
        print(r2)
        self.assertEqual(r2[0][0], 'test')

    def tearDown(self):
        """
        Delete the database
        """

        sql = "DROP DATABASE mydb"
        db.MySQLdb_connection.query_db(sql)
        r = db.MySQLdb_connection.query_db("SHOW DATABASES LIKE '%s'" % 'mydb')

        # self.assertEqual(r[0][0], 'mydb')
        print('tearDown...')


    def test_insert(self):
        """
        Tests that we can successfully insert
        """

        sql = "INSERT INTO test (name, salary) VALUES ('%s', '%s')" % \
        ('John', 60000)
        db.MySQLdb_connection.query_db(sql, db_use = 'mydb')
        sql = "INSERT INTO test (name, salary) VALUES ('%s', '%s')" % \
        ('Tony', 50000)
        db.MySQLdb_connection.query_db(sql, db_use = 'mydb')
        sql = "INSERT INTO test (name, salary) VALUES ('%s', '%s')" % \
        ('Chris', 70000)
        r2 = db.MySQLdb_connection.query_db(sql, db_use = 'mydb')
        # self.assertEqual(r2, ())

        sql = "SELECT * FROM test"
        r2 = db.MySQLdb_connection.query_db(sql, 'mydb')
        #print(r2)
        self.assertEqual(r2[0][1], 'John')

    def test_update(self):
        """
        Tests that we can successfully update
        """

        sql = "INSERT INTO test (name, salary) VALUES ('%s', '%s')" % \
        ('Chris', 70000)
        r2 = db.MySQLdb_connection.query_db(sql, db_use = 'mydb')

        sql = "UPDATE test SET salary = 300 WHERE name = 'Chris'"
        db.MySQLdb_connection.query_db(sql, db_use = 'mydb')
        sql = "SELECT * FROM test WHERE name = 'Chris'"
        r2 = db.MySQLdb_connection.query_db(sql, 'mydb')
        #print(r2)
        self.assertEqual(r2[0][2], 300)

    def test_delete(self):
        """
        Tests that we can successfully delete
        """

        sql = "INSERT INTO test (name, salary) VALUES ('%s', '%s')" % \
        ('John', 70000)
        r2 = db.MySQLdb_connection.query_db(sql, db_use = 'mydb')

        sql = "DELETE FROM test WHERE name = 'John'"
        db.MySQLdb_connection.query_db(sql, db_use = 'mydb')
        sql = "SELECT * FROM test WHERE name = 'John'"
        r2 = db.MySQLdb_connection.query_db(sql, 'mydb')
        #print(r2)
        self.assertEqual(r2, 0)


    # def test_insert_update_delete(self):
    #     """
    #     Tests that we can successfully insert, update, delete
    #     """
    #
    #     sql = "INSERT INTO test (name, salary) VALUES ('%s', '%s')" % \
    #     ('John', 60000)
    #     r2 = db.MySQLdb_connection.query_db(sql, db_use = 'mydb')
    #     self.assertEqual(r2, ())
    #
    #     sql = "SELECT * FROM test WHERE name = 'John'"
    #     r2 = db.MySQLdb_connection.query_db(sql, 'mydb')
    #     #print(r2)
    #     self.assertEqual(r2[0][1], 'John')
    #
    #     sql = "UPDATE test SET salary = 300"
    #     db.MySQLdb_connection.query_db(sql, db_use = 'mydb')
    #     sql = "SELECT * FROM test WHERE name = 'John'"
    #     r2 = db.MySQLdb_connection.query_db(sql, 'mydb')
    #     #print(r2)
    #     self.assertEqual(r2[0][2], 300)
    #
    #     sql = "DELETE FROM test WHERE name = 'John'"
    #     db.MySQLdb_connection.query_db(sql, db_use = 'mydb')
    #     sql = "SELECT * FROM test WHERE name = 'John'"
    #     r2 = db.MySQLdb_connection.query_db(sql, 'mydb')
    #     #print(r2)
    #     self.assertEqual(r2, 0)


"""
Return Values

For SELECT, SHOW, DESCRIBE, EXPLAIN and other statements returning resultset,
mysql_query() returns a resource on success, or FALSE on error.

For other type of SQL statements, INSERT, UPDATE, DELETE, DROP, etc,
mysql_query() returns TRUE(1) on success or FALSE(0) on error.
"""
