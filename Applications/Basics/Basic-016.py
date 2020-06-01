# Write a Python program to get the difference between a given number and 17, if the number is greater than 17 return double the absolute difference.
num = int(input("Please enter an integer : "))

if (num > 17):
    print((num-17)*2)
elif (num < 17):
    print(abs(num-17))