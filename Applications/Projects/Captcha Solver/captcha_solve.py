# Python program to illustrate HoughLine 
# method for line detection 
from cv2 import cv2 
import numpy as np 
  
# Reading the required image in  
# which operations are to be done.  
# Make sure that the image is in the same  
# directory in which this python program is 
img = cv2.imread('3.png') 
  
# Convert the img to grayscale 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) 
cv2.imshow("",gray)
cv2.waitKey(0)
# Apply edge detection method on the image 
edges = cv2.Canny(gray,1000,350,apertureSize = 3) 

# This returns an array of r and theta values 
lines = cv2.HoughLines(edges,1,np.pi/180, 200) 
    
cv2.imshow("",edges)
cv2.waitKey(0)
cv2.destroyAllWindows()