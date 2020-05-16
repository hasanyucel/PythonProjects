# Write a Python program to concatenate all elements in a list into a string and return it.

lst = [1,2,3,4,5,5,1,2,4]
st = ""
for number in lst:
    st = st + str(number)

print(st)