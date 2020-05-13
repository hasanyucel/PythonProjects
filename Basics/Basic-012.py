# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module.

import calendar
month = int(input("Please enter month : "))
year = int(input("Please enter year : "))
print(calendar.month(year, month))