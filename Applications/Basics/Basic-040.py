# Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
import math
def dist_two_point(point1,point2):
    distance = pow(abs(point1[0]-point2[0]),2)+pow(abs(point1[1]-point2[1]),2)

    return math.sqrt(distance)

p1 = [2,3]
p2 = [8,11]
print(dist_two_point(p1,p2))