# Write a Python program to create a SQLite database and connect with the database and print the version of the SQLite database.

import sqlite3
conn = sqlite3.connect('firstdatabase.db')
conn.close()