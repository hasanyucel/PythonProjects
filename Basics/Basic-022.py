# Write a Python program to count the number 4 in a given list.

lst = [3,2,1,4,5,6,9,4,6,4]
counter = 0
for num in lst:
    if num==4:
        counter=counter+1

print(counter)