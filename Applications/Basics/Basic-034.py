# Write a Python program to sum of two given integers. However, if the sum is between 15 to 20 it will return 20.

def sum_of_two_integers(num1,num2):
    sumInts = num1 + num2
    if(sumInts<20 and sumInts > 15):
        return 0
    else:
        return sumInts

print(sum_of_two_integers(6,9))
print(sum_of_two_integers(10,10))
print(sum_of_two_integers(7,9))