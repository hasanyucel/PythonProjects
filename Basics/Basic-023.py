# Write a Python program to get the n (non-negative integer) copies of the first 2 characters of a given string. Return the n copies of the whole string if the length is less than 2.

def n_copy(str,n):
    if len(str) < 2:
        return str*n
    else:
        return (str[0:2]*(n))+str

print(n_copy("test",3))