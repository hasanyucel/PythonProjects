import numpy as np
from cv2 import cv2

img = cv2.imread('5.png')
cv2.imshow("img",img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)


thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
cv2.imshow("thresh",thresh)

line = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("line",line)

kernel = np.ones((3,2),np.uint8)
dilation = cv2.dilate(line,kernel,iterations = 1)
cv2.imshow("dilation",dilation)

res = thresh+dilation
cv2.imshow("res",res)

kernel2 = np.ones((2,2),np.uint8)
erode = cv2.erode(gray,kernel2,iterations = 1)
cv2.imshow("erode",erode)

kernel2 = np.ones((2,2),np.uint8)
d2 = cv2.dilate(erode,kernel2,iterations = 1)
cv2.imshow("d2",d2)

cv2.waitKey(0)
cv2.destroyAllWindows()

# mask = cv2.compare(gray,50,cv2.CMP_LT)
# cv2.imshow("mask",mask)
# img[mask > 0] = 255
# cv2.imshow("img2",img)


# thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# cv2.imshow("thresh",thresh)

# line = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY_INV)[1]
# cv2.imshow("line",line)

# kernel = np.ones((3,2),np.uint8)
# dilation = cv2.dilate(line,kernel,iterations = 1)
# cv2.imshow("dilation",dilation)

# res = thresh+dilation
# cv2.imshow("res",res)

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow("gray",gray)

# mask = cv2.compare(gray,50,cv2.CMP_LT)
# cv2.imshow("mask",mask)
# img[mask > 0] = 255
# cv2.imshow("img2",img)

# for i in range(46):
#     for j in range (240):
#         if(img[i,j][0] < 70 or img[i,j][0] > 190):
#             img[i,j] = 255
# cv2.imshow("",img)