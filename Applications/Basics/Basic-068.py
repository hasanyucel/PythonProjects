# Write a Python program to calculate the sum of the digits in an integer.

num = int(input("Please Enter a Number: "))

number_string = str(num)
sumnum=0
for ch in number_string:
    sumnum = sumnum + int(ch)
print("Sum of digits in ",number_string," is : ",sumnum)

#w3sources answer (is it limited with 4 digit. First solution is better.)
num = int(input("Input a four digit numbers: "))
x  = num //1000
x1 = (num - x*1000)//100
x2 = (num - x*1000 - x1*100)//10
x3 = num - x*1000 - x1*100 - x2*10
print("The sum of digits in the number is", x+x1+x2+x3)