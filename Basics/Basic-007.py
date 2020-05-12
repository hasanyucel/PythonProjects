# Write a Python program to accept a filename from the user and print the extension of that.
# Sample filename : abc.java
# Output : java

filename = input("Please enter file name: ")
ext = filename.split(".")
print(ext[-1])