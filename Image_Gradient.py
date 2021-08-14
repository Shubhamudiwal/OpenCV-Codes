#Image Gradient
#It is a directional change in the color or intensity in an image.
#It is most important part to find information from image.
#Like finding edges within the images
#There are various methods to find image gradient.
#These are - Laplacian Derivatives, SobeLX and SobeLY.
#All these functions have diff. Methematical approach to get result.
#All Load image in the gray scale.

import cv2
import numpy as np
 


#Load image into gray scale

img = cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\avengers.jpg")
img = cv2.resize(img,(400,400))
img_gray= cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Laplacian Derivative -- It calculate Laplace derrivate
#parameter(img, data_type for -ve val, ksize)
lap =  cv2.Laplacian(img_gray,cv2.CV_64F,ksize = 3)
lap =  np.uint8(np.absolute(lap))

#Sobel operation -
#It is a joint Gaussian smoothing plus differentiation operation, 
#so it is more resistant to noise
# This is use for x and y both
# parameter (img,type for -ve val, x = 1, y=0 , ksize)
#Sobel X focus on vertical lines
#Sobel Y focus on horizontal lines

sobelx = cv2.Sobel(img_gray,cv2.CV_64F,1,0,ksize = 3) 
sobely = cv2.Sobel(img_gray,cv2.CV_64F,0,1,ksize = 3) 

sobelx = np.uint8(np.absolute(sobelx))
sobely = np.uint8(np.absolute(sobely))

#finally combine sobelX and sobelY together
sobelcombine = cv2.bitwise_or(sobelx,sobely)





cv2.imshow("original ==",img)
cv2.imshow("gray ==",img_gray)
cv2.imshow("Laplacian ==",lap)
cv2.imshow("Sobelx==",sobelx)
cv2.imshow("Sobely==",sobely)
cv2.imshow("Sobelcombine ==",sobelcombine)

cv2.waitKey(0)
cv2.destroyAllWindows()