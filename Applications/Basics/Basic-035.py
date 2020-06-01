# Write a Python program that will return true if the two given integer values are equal or their sum or difference is 5.

def int_sum_dif(num1,num2):
    if(num1==num2):
        return True
    
    elif(abs(num1-num2)==5 or abs(num1+num2)==5):
        return True
    
    else:
        return False

print(int_sum_dif(7,1))
print(int_sum_dif(6,1))
print(int_sum_dif(4,1))
print(int_sum_dif(1,1))
print(int_sum_dif(7,15))
