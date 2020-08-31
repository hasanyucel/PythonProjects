import numpy as np
from cv2 import cv2

img = cv2.imread('captchas/10.png')
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

thresh = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY)[1]
img = cv2.bitwise_not(thresh)
num_labels, labels_im, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity=4, ltype=cv2.CV_32S)
for i in range(1, num_labels):
    if stats[i][4] <= 20:
        img[labels_im == i] = 0
img = cv2.medianBlur(img, 3)
img = cv2.GaussianBlur(img, (3, 3), 0)
cv2.imshow('result.png', img)

cv2.waitKey(0)
cv2.destroyAllWindows()