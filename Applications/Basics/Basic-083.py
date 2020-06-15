# Write a Python program to test whether all numbers of a list is greater than a certain number.

def greater_or_not(number):
    lst = [5,6,7]
    for num in lst:
        if(number <= num):          
            return False
    return True

    
print(greater_or_not(9))