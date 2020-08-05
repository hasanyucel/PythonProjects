# Write a Python program to calculate the time runs (difference between start and current time) of a program.

import datetime
import time

strt = (datetime.datetime.now)
print(strt())
for i in range(0,10):
    time.sleep(0.1)
end = (datetime.datetime.now) 
print(end())

#w3sources answer
from timeit import default_timer
def timer(n):
    start = default_timer()
    # some code here
    for row in range(0,n):
        print(row)
    print(default_timer() - start)

timer(5)
timer(15)