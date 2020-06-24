# Write a Python program to swap two variables.

#swap with 1 temp variable
fn = 10
sn = 20
temp = fn
fn = sn 
sn = temp

#swap without temp variable(python feature)
a = 10
b = 20
print(a,b)
a,b = b,a 
print(a,b)

#swap without temp variable
x = 10
y = 20
x = x + y #x=30 (10+20)    
y = x - y #y=10 (30-20)    
x = x - y #x=20 (30-10)  