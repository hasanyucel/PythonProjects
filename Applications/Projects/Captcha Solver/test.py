import numpy as np
from cv2 import cv2
import pytesseract
from PIL import Image


# Load image, grayscale, adaptive threshold
image = cv2.imread('captchas/10.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,3)

# Morph open
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (4,3))
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)

# Remove noise by filtering using contour area
cnts = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for c in cnts:
    area = cv2.contourArea(c)
    if area < 10:
        cv2.drawContours(opening, [c], -1, (0,0,0), -1)

# Invert image for result
result = 255 - opening

cv2.imshow('thresh', thresh)
cv2.imshow('opening', opening)
cv2.imshow('result', result)

cv2.imwrite("result2.png",result)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
a=pytesseract.image_to_string(Image.open('result2.png'))
print(a)

# cv2.waitKey()
# img = cv2.imread('captchas/10.png')
# img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# thresh = cv2.threshold(img, 40, 255, cv2.THRESH_BINARY)[1]
# img = cv2.bitwise_not(thresh)
# num_labels, labels_im, stats, centroids = cv2.connectedComponentsWithStats(img, connectivity=4, ltype=cv2.CV_32S)
# for i in range(1, num_labels):
#     if stats[i][4] <= 20:
#         img[labels_im == i] = 0
# img = cv2.medianBlur(img, 3)
# img = cv2.GaussianBlur(img, (3, 3), 0)
# cv2.imshow('result.png', img)

cv2.waitKey(0)
cv2.destroyAllWindows()