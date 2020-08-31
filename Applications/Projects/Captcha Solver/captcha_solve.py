import numpy as np
from cv2 import cv2

img = cv2.imread('captchas/5.png')
cv2.imshow("img",img)

croppedImg = img[0:46, 10:190]
cv2.imshow("croppedImg",croppedImg)

filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
sharpen_img = cv2.filter2D(croppedImg,-1,filter)
cv2.imshow("sharpen_img",sharpen_img)

gray = cv2.cvtColor(sharpen_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)

# thresh = cv2.threshold(gray, 30, 255, cv2.THRESH_BINARY)[1]
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,60)
cv2.imshow("thresh",thresh)

line = cv2.threshold(croppedImg, 20, 255, cv2.THRESH_BINARY_INV)[1]
cv2.imshow("line",line)
line = cv2.cvtColor(line, cv2.COLOR_BGR2GRAY)

res = thresh+line
cv2.imshow("res",res)

cv2.waitKey(0)
cv2.destroyAllWindows()




# thresh = cv2.adaptiveThreshold(erode,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)
# cv2.imshow("thresh",thresh)

# line = cv2.threshold(gray, 40, 255, cv2.THRESH_BINARY_INV)[1]
# cv2.imshow("line",line)

# kernel = np.ones((3,2),np.uint8)
# dilation = cv2.dilate(line,kernel,iterations = 1)
# cv2.imshow("dilation",dilation)

# res = thresh+dilation
# cv2.imshow("res",res)

# kernel2 = np.ones((2,2),np.uint8)
# d2 = cv2.dilate(res,kernel2,iterations = 1)
# cv2.imshow("d2",d2)

# kernel2 = np.ones((2,2),np.uint8)
# e2 = cv2.erode(d2,kernel2,iterations = 1)
# cv2.imshow("e2",e2)

# num_labels, labels_im, stats, centroids = cv2.connectedComponentsWithStats(e2, connectivity=4, ltype=cv2.CV_32S)
# for i in range(1, num_labels):
#     if stats[i][4] <= 20:
#         e2[labels_im == i] = 0
# e2 = cv2.medianBlur(e2, 3)
# e2 = cv2.GaussianBlur(e2, (3, 3), 0)
# cv2.imshow('result.png', e2)


# filter = np.array([[-1, -1, -1], [-1, 9, -1], [-1, -1, -1]])
# # Applying cv2.filter2D function on our Cybertruck image
# sharpen_img_1=cv2.filter2D(e2,-1,filter)
# cv2.imshow("sharpen_img_1",sharpen_img_1)



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