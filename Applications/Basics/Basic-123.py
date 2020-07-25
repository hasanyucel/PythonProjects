# Write a Python program to determine the largest and smallest integers, longs, floats.
import sys 

maxint = sys.maxsize
minint = -sys.maxsize
intval = sys.int_info
floatval = sys.float_info
print(intval,floatval)