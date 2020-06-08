# Write a Python program to calculate midpoints of a line.

def cal_mid(p1,p2):
    return (abs(p1[0])+abs(p2[0]))/2,(abs(p1[1])+abs(p2[1]))/2

print(cal_mid([8,8],[8,8]))
print(cal_mid([0,0],[6,0]))