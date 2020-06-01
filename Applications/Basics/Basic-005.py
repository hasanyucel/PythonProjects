# Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.

fName = input("Please enter your first name: ")
lName = input("Please enter your last name: ")
print(fName[::-1],lName[::-1])