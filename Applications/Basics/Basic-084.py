# Write a Python program to count the number occurrence of a specific character in a string.

def occ_char(text,chra):
    counter = 0
    chars = []
    chars[:] = text 
    for ch in chars:
        if ch == chra:
            counter = counter + 1
    return counter


print(occ_char('hasan','s'))

#w3sources answer (too easy :))
s = "hasan"
print(s.count("a"))