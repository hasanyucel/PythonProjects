# Write a Python program to calculate midpoints of a line.

def cal_mid(p1,p2):
    return (abs(p1[0])+abs(p2[0]))/2,(abs(p1[1])+abs(p2[1]))/2

print(cal_mid([8,8],[8,8]))
print(cal_mid([0,0],[6,0]))


#w3sources answer
print('\nCalculate the midpoint of a line :')

x1 = float(input('The value of x (the first endpoint) '))
y1 = float(input('The value of y (the first endpoint) '))

x2 = float(input('The value of x (the first endpoint) '))
y2 = float(input('The value of y (the first endpoint) '))

x_m_point = (x1 + x2)/2
y_m_point = (y1 + y2)/2
print();
print("The midpoint of line is :")
print( "The midpoint's x value is: ",x_m_point)
print( "The midpoint's y value is: ",y_m_point)
print();