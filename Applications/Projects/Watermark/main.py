import cv2
import numpy as np
#importing the main image
image = cv2.imread('floWer.jpg')
oH,oW = image.shape[:2]
image = np.dstack([image, np.ones((oH,oW), dtype="uint8") * 255])

#importing the logo image
lgo_img = cv2.imread('logo.png',cv2.IMREAD_UNCHANGED)

#Resizing the image
scl = 10
w = int(lgo_img.shape[1] * scl / 100)
h = int(lgo_img.shape[0] * scl / 100)
dim = (w,h)
lgo = cv2.resize(lgo_img, dim, interpolation = cv2.INTER_AREA)
lH,lW = lgo.shape[:2]

#Blending
ovr = np.zeros((oH,oW,4), dtype="uint8")
ovr[oH - lH - 60:oH - 60, oW - lW - 10:oW - 10] = lgo
final = image.copy()
final = cv2.addWeighted(ovr,0.5,final,1.0,0,final)


# ShoWing the result
cv2.imshow("Combine Image",final)
cv2.waitKey(0)
cv2.destroyAllWindows()