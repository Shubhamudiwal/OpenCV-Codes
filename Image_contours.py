#Contours-

#Contours can be explained simply as curve joining all the continuous points 
#(along the boundary),having same color or intensity

#The contours are a useful tool for shape anaalysis and object detection and recognition

#For better accuracy, use binary images and also apply edge detection before finding countours.

#find Countours function manipulate original iamge so copy it before proceeding.
#find Contour is like finding white object from black background.
#so you must turn image in white and background in black.

#We have to find and draw contours as per the requirement.


import cv2
import numpy as np

img = cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\logo.jpg") 
img1= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,thresh = cv2.threshold(img1,20,255,0)

#find contour(img,contour_retrival_mode, method)
cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

print(cnts,len(cnts))


#drawcontour(img,cnts,id of contour, color, thickness)here if we draw
#contour just pass -1
#Draw the contours
img= cv2.drawContours(img,cnts,-1,(176,10,15),4) 

#output

cv2.imshow("original ==",img)
cv2.imshow("gray==",img1)
cv2.imshow("threshold",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
