# Write a Python program to create a SQLite database connection to a database that resides in the memory.

import sqlite3
try:
   sqlite_Connection = sqlite3.connect('temp.db')
   conn = sqlite3.connect(':memory:')
   print("\nMemory database created and connected to SQLite.")
   sqlite_select_Query = "select sqlite_version();"
   conn.execute(sqlite_select_Query)
   print("\nSQLite Database Version is: ", sqlite3.version)
   conn.close()
except sqlite3.Error as error:
   print("\nError while connecting to sqlite", error)
finally:
   if (sqlite_Connection):
       sqlite_Connection.close()
       print("\nThe SQLite connection is closed.")