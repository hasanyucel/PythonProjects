# Write a Python program to compute the greatest common divisor (GCD) of two positive integers.

def find_GCD(num1, num2):
    gcd = 1
    if num1 % num2 == 0:
        return num2
    
    for i in range(int(num2 / 2), 0, -1):
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
            break  
    return gcd

print(find_GCD(16, 24))
