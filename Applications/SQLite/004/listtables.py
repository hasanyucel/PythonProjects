# Write a Python program to list the tables of given SQLite database file.

import sqlite3
conn = sqlite3.connect('newdb.db')
cursor = conn.cursor()
#cursor.execute( """CREATE TABLE test(test char(6),commission decimal(10,2),phone_no char(15) NULL);""" )
#cursor.execute( """CREATE TABLE test2(test char(6),commission decimal(10,2),phone_no char(15) NULL);""" )
#cursor.execute( """CREATE TABLE test3(test char(6),commission decimal(10,2),phone_no char(15) NULL);""" )
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())
conn.commit()
conn.close ()