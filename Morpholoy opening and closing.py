##Morphological transformations are some simple operations based on the image shapes
#It is normally performed on binary images.
#It needs two inputs, 1)original image, 2)structuring element(kernel)
# Two basic Morphological Transformations are 1) Opening and 2) Closing

import cv2
import numpy as np

#Opening --
#Opening is just another name of erosion followed by dilation.
#Means first erosion take place then dilation

img =  cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\col_balls.jpg",0)

_,mask =  cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((4,4),np.uint8)#5x5 kernal with full of ones.
o =  cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel) #Optional parameter iterations = 2


#Closing --
#Closing is just another name of dilation followed by erosion.
#Means first dilation take place then erosion

_,mask =  cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((4,4),np.uint8)#5x5 kernal with full of ones.
c =  cv2.morphologyEx(mask,cv2.MORPH_CLOSE ,kernel) #Optional parameter iterations = 2


cv2.imshow("image",img)
cv2.imshow("kernal",kernel)
cv2.imshow("mask", mask)
cv2.imshow("Openings",o)
cv2.imshow("Closing",c)

# from matplotlib import pyplot as plt
# titles  =["img","mask","Openings"]

# images=[img,mask,o]
# for i in range(4):
#     plt.subplot(2,2,i+1)
#     plt.imshow(images[i],'gray')
#     plt.title(titles[i])
#     plt.xticks([]),plt.yticks([])

#plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()