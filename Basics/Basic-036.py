# Write a Python program to add two objects if both objects are an integer type.

def sum_two_integers(num1, num2):
    if (isinstance(num1, int) and isinstance(num2, int)):
        return num1 + num2
    else:
        return "They are not integer"

print(sum_two_integers(10, 20))