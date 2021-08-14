#Thresholding
#Thresholding is of major 2 type - Simple thresholding,Adaptive thresholding,
#Simple thresholding(img,pixel_thresh,_max_thresh_pixel,style)


import cv2
import numpy as np

img = cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\black_white.png",0)
img =cv2.resize(img,(300,300))
cv2.imshow("Original",img)

_, th1 = cv2.threshold(img,50,255,cv2.THRESH_BINARY_INV)
_, th2 = cv2.threshold(img,50,255,cv2.THRESH_BINARY)
_,th3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
_,th4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
_,th5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)

510
cv2.imshow("1- THRESH_BINARY",th1)
cv2.imshow("1- THRESH_BINARY_INV",th2)
cv2.imshow("1- THRESH_BINARY_TRUNC",th3)
cv2.imshow("1- THRESH_TOZERO",th4)
cv2.imshow("1- THRESH_TOZERO_INV",th5)
cv2.waitKey(0)
cv2.destroyAllWindows()