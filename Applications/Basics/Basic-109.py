# Write a Python program to check if a number is positive, negative or zero.

def pos_neg_or_zero(num):
    if (num == 0):
        return "The number is zero."
    elif (num < 0):
        return "The number is negative."
    elif (num > 0):
        return "The number is positive"

num = int(input("Please enter a number: "))
print(pos_neg_or_zero(num))