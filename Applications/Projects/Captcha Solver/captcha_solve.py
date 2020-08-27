import numpy as np
from cv2 import cv2

img = cv2.imread('2.png')
cv2.imshow("img",img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("thresh",thresh)

line = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("line",line)

res = thresh+line
cv2.imshow("res",res)

cv2.waitKey(0)
cv2.destroyAllWindows()