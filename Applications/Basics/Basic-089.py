# Write a Python program to perform an action if a condition is true.
# Given a variable name, if the value is 1, display the string "First day of a Month!" and do nothing if the value is not equal.
import datetime 

def ifTrue(str1):
    if(str1 == "1"):
        firstDay = datetime.date.today().replace(day=1)
        print(firstDay)

ifTrue("1")

#w3sources answer
n=1
if n == 1:
    print("\nFirst day of a month")
print()