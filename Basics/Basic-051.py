# Write a Python program to determine profiling of Python programs.

# Note: A profile is a set of statistics that describes how often and for how long various parts of the program executed. These statistics can be formatted into reports via the pstats module.

import cProfile
def sum():
    print(1+2)
cProfile.run('sum()')