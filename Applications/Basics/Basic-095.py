# Write a Python program to check whether a string is numeric. 



def nos(num_or_str):
    if(num_or_str.isnumeric()):
        return "Numeric"
    else:
        return "String"

num_or_str = input("Please enter an input: ")
print(nos(num_or_str))