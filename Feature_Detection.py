#feature Detection and Description

#Corner Detection

"""
For understanding this we recall jisaw puzzle game where we combine multiple small 
pieces in correct order by identifying its corners, shpe and patttern.

On the basia of all thsese we all detect corners in images with so many approaches.


"""
#Harris Corner Detection

"""
OpenCV has the function cv2.cornerHarris() for this purpose. Its arguments are

img- Input image, it should be grayscale and float32 type.
blockSize - It is the size of neighbourhood considered for corner detection.
ksize- aperture parameter of Sobel derivative used.
k - Harris detector free parameter in the equation.

"""

"""
import cv2
import numpy as np

img = cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\shapes.png")

#gray--
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)


#detect corner
res= cv2.cornerHarris(gray,2,3,0.04)

res = cv2.dilate(res,None)

img[res>0.01*res.max()]=[0,0,255]#marked color

cv2.imshow("img",img)
#cv2.imshow("rseult",res)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""

#We will learn about the another corner detector:Shi-Tomasi Corner Detector
#We will see the function: cv2.goodFeaturesaaToTrack()
#Shi - Tomasi approach is more effective as compared with Harris Corner detector

#In this we limit the number of corner and corners quality.
#It is more user friendly.

import numpy as np
import cv2 


img = cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\shapes.png")

#Imgae must be in gray

#gray--
gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Parameter(img,no. of corner, quality_level,min_distance between corner)
corners = cv2.goodFeaturesToTrack(gray,50,0.01,10)
corners = np.int64(corners)

for i in corners:
    x,y = i.ravel()
    cv2.circle(img,(x,y),3,255,-1)
    
cv2.imshow("res==",img)
cv2.waitKey(0)

cv2.destroyAllWindows()


