"""
It is a method for searching and finding the location of a template image in a large image
OpenCV comes with a function cv2.matchTemplate() for this purpose.
It is simply slides the template image over the input image(as in 2D convolution)
and compares the template and patch of input image under the template image.
"""

import cv2
import numpy as np

img = cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\avengers.jpg")
img_gray= cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#Load template

template =cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\iron_head.jpg",0)

w, h = template.shape[::-1]

#template matching
#this fnction accept parameters (img, template,method)
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCORR_NORMED)
print(res)

threshold = 0.999
loc = np.where(res>=threshold)#Finding brightest pixel

for i in zip(*loc[::-1]):
    print("i==",i)
    cv2.rectangle(img,i,(i[0]+w,i[1]+h),(0,0,255),2)

res = cv2.resize(res,(800,600))
img = cv2.resize(img,(800,600))
cv2.imshow("img",img)
cv2.imshow("result",res)



cv2.waitKey(0)
cv2.destroyAllWindows() 