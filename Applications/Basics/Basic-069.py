# Write a Python program to sort three integers without using conditional statements and loops.

def sort_integers(numbers):
    numbers.sort()
    print(numbers)

sort_integers([1,3,2,5,5,6,3,2,1])

# w3sources answer

x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)