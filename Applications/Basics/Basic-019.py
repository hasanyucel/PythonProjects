# Write a Python program to get a new string from a given string where "Is" has been added to the front. If the given string already begins with "Is" then return the string unchanged.

def st_change(st):
    if st[0:2] == "Is":
        return st
    else:
        return "Is"+st

print(st_change("Test"))
print(st_change("Isasd"))