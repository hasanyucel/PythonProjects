# Write a Python program which accepts a sequence of comma-separated numbers from user and generate a list and a tuple with those numbers.
# Sample data : 3, 5, 7, 23
# Output :
# List : ['3', ' 5', ' 7', ' 23']
# Tuple : ('3', ' 5', ' 7', ' 23')

numbers = input("Please enter numbers: ")
li = list(numbers.split(","))
tu = tuple(numbers.split(","))
print("List: ",li)
print("Tuple: ",tu)