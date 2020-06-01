# Write a Python program to display the current date and time.

import datetime

datenow = datetime.datetime.now()
print (datenow.strftime("%Y-%m-%d %H:%M:%S"))