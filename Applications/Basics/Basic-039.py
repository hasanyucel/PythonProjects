# Write a Python program to compute the future value of a specified principal amount, rate of interest, and a number of years.

def future_value(amount,roint,years):
    return amount*((1+(0.01*roint)) ** years)

print(round(future_value(10000,3.5,7),2))

