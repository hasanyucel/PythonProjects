# Write a Python program to convert height (in feet and inches) to centimeters.

def convert_height(feet,inch):
    return (feet*30.48) + (inch*2.54)
    
print(convert_height(5,3),"cm")
