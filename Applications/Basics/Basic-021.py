# Write a Python program to find whether a given number (accept from the user) is even or odd, print out an appropriate message to the user.

def even_odd(num):
    if abs(num) % 2 == 0:
        return "The number is even."
    else:
        return "The number is odd."

num = int(input("Please enter a number : "))
print(even_odd(num))