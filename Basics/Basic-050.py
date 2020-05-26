# Write a Python program to print without newline or space.

def no_space_newline(str):
    str = str.replace(" ","")
    str = str.replace("\n","")
    print(str)

no_space_newline("test asd\nasd qwe")

# w3resource solution 

for i in range(0, 15):
    print('*', end="")
print("\n")