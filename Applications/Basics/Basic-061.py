# Write a Python program to convert the distance (in feet) to inches, yards, and miles.

def convert_feet(feet):
    print(feet," feet =",feet*12," inches")
    print(feet," feet =",round(feet*0.333333333333,4)," yards")
    print(feet," feet =",round(feet*0.000189393939,4)," miles")

convert_feet(100)