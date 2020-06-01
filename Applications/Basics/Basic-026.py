# Write a Python program to create a histogram from a given list of integers.

lst = [1,2,3,4,5,5,1,2]

for number in lst:
    print(lst[number-1]*"*")