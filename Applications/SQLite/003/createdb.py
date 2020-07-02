import  sqlite3

conn = sqlite3.connect('newdb.db')
cursor = conn.cursor()
cursor.execute( """CREATE TABLE test(test char(6),commission decimal(10,2),phone_no char(15) NULL);""" )
conn . close ()
