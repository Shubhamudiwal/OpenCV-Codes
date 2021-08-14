#Morphological transformations

#Morphological transformations are some simple operations based on the image shapes
#It is normally performed on binary images.
#It needs two inputs, 1)original image, 2)structuring element(kernel)
# Two basic Morphological Transformations are 1) Erosion and 2) Dialation

import cv2
import numpy as np

#Erosion
# It erodes away the boundaries of foreground object

#Kernal slides through all the image and all the pixel
#from the original image conside 1 only if kernal's pixel is 1
img =  cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\col_balls.jpg",0)

_,mask =  cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8)#5x5 kernal with full of ones.
e = cv2.erode(mask,kernel)


#Dilation
#It is just opposite of erosion
#Here, a pixel is '1' if atleast one pixel under the kernel is '1'
#SO it inc. white region in the image or size of foreground object in.
#Normally, in cases like noise removal, erosion is followed by dilation.
#Because,erosion removes white noises, but it also shrinks our object.

kernel = np.ones((5,5),np.uint8)#5x5 kernal with full of ones.
d = cv2.dilate(mask,kernel)

cv2.imshow("image",img)
#cv2.imshow("kernal",kernel)
cv2.imshow("mask", mask)
cv2.imshow("erosion",e)
cv2.imshow("dilation",d)


#if you want then plot it

from matplotlib import pyplot as plt
titles  =["img","mask","erosion","dilation"]

images=[img,mask,e,d]
for i in range(4):
    plt.subplot(2,2,i+1)
    plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()

