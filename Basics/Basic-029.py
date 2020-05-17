# Write a Python program to print out a set containing all the colors from color_list_1 which are not present in color_list_2. Go to the editor
# Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
# Expected Output :
# {'Black', 'White'}

#*First solution 
for color1 in color_list_1:
    if(color_list_2.__contains__(color1)):
        pass
    else:
        print(color1)

#*Second solution from w3resource 
print(color_list_1.difference(color_list_2))