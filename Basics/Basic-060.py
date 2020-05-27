# Write a Python program to calculate the hypotenuse of a right angled triangle. 
import math
def find_hypotenuse(a,b):
    c = (a**2) + (b**2)
    return math.sqrt(c)

print(find_hypotenuse(3,4))