# Write a Python program to check whether a specified value is contained in a group of values. 
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

lst = [1, 5, 8, 3]

def contined_or_not(num):
    if  lst.__contains__(num):
        return True
    else:
        return False

print(contined_or_not(3))
print(contined_or_not(-1))