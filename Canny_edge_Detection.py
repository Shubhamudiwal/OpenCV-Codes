#Canny Edge Detection using OpenCV
#Canny Edge Dedection is a popu;ar edge detection approach.
#It is used for multi-stage algorithm to detect a edges.
# It was developed by John F. Canny in 1986
# this approach combine with 5 steps.
#1) Noise reduction(gauss),2) Gradient calculation
#3) Non maximum suppression, 4) Double Threshold,
#5) Edge Tracking by Hysteresis

import cv2
import numpy as np

"""
#Load image into gray scale
img = cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\building.jpg")
img = cv2.resize(img,(600,600))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Parameter fir canny 
#canny(img,thresh1,thresh2),thresh 1 and thresh2 at different lvl

canny = cv2.Canny(img_gray,100,200)

cv2.imshow("Original",img)
cv2.imshow("gray ==",img_gray)
cv2.imshow("Canny==",canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
"""

img = cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\building.jpg")
img = cv2.resize(img,(600,600))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


def nothing(x):
    pass

cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold","Canny",0,255,nothing)
while True:
    a= cv2.getTrackbarPos("Threshold","Canny")
    print(a)
    res = cv2.Canny(img_gray,a,255)
    cv2.imshow("Canny",res)
    k =cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    
cv2.destroyAllWindows()