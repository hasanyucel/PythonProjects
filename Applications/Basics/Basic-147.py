# Write a Python function to check whether a number is divisible by another number. Accept two integers values form the user.

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter First Number: "))

if(num1 % num2 == 0):
    print("First number can divide by second number.")
if(num2 % num1 == 0):
    print("Second number can divide by first number.")

# w3sources answer
def multiple(m, n):
	return True if m % n == 0 else False

print(multiple(20, 5))
print(multiple(7, 2))