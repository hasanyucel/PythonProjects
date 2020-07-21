# Write a Python program to input a number, if it is not a number generate an error message.

num = input("Enter a number: ")

try:
   val = int(num)
except ValueError:
   print("This is not a number!")