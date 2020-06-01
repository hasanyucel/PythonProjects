# Write a Python program to get the least common multiple (LCM) of two positive integers.

def find_LCM(num1, num2):
    if num1 > num2:
       temp = num1
    else:
       temp = num2

    while(True):
       if((temp % num1 == 0) and (temp % num2 == 0)):
           lcm = temp
           break
       temp += 1

    return lcm

print(find_LCM(12, 5))