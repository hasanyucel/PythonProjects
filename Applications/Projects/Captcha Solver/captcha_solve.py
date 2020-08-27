import numpy as np
from cv2 import cv2

image = cv2.imread('2.png')
cv2.imshow("image",image)

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) 
cv2.imshow("gri",gray)

cizgi = cv2.threshold(gray, 40, 200, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("cizgi",cizgi)

res = gray+cizgi
cv2.imshow("res",res)

other = cv2.threshold(res, 60, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("other",other)


cv2.waitKey(0)
cv2.destroyAllWindows()