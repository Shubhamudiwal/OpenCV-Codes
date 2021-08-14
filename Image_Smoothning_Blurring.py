#Image Smoothing or blurring is most common used operation in Image Processing.
#It is used to remove noise from the images.
#There are so many filter which is used for smoothing the image.
#There are Low pass filter (LPS) which use to remove Noise from the images.
#There are High Pass Filter which used to detect and finding edges in an images.

#we discuss about various filters
#like, Homogeneous,blur(averaging), gaussian, median, bo;ateral


import cv2
import numpy as np

img = cv2.imread('C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\noisy2.jpg',0)
img = cv2.resize(img,(200,200))
cv2.imshow("image",img)

kernel = np.ones((5,5),np.float32)/25

#Filter No. 1
# this filter work like, each output pixel is the mean of its kernal neighbour
#it is aka homogeneous filter in this all pixel contribute with equal weight.
#kernal is small shape or matrix which we apply on image.
#in this filter kernal is [(1/kernal(h,w))*kernal]]
h_filter  = cv2.filter2D(img,-1,kernel) #-1 is desired depth
cv2.imshow("homogeneous ==",h_filter)

#Filter No. 2
#blur method or averaging
#Takes the avg of all the pixel under kernel area and
#replaces the central element with this average.
blur = cv2.blur(img,(5,5))
cv2.imshow("blur==",blur)

#Filter No. 3
#Gaussian Filter -here it using different weight kernel, in row as well as column
##neabs side values are smaller then centre . It manage distance between values of pixel

gau =  cv2.GaussianBlur(img,(5,5),0) #here 0 is sigma x value
cv2.imshow("gau Blur == ",gau)

#Filter No. 4
#Median Filter -- computes the median of all the pixel under the
# kernel window and central pixel is replaced with this median values.
# This is highly effective in removing salt and pepper noise.
#Here kernel size must be odd except one.

med =  cv2.medianBlur(img,5)
cv2.imshow("median filter==",med)

#Filter No.5
#Bilateral filter is highly effective at noise removal while preserving edges 
#It work like gaussian filter but more focus on  edges
#It is slow as compare with other filters
#argument (img, neighbour_pixel_dia,sigma_color,sigma_spaces)
bi_f = cv2.bilateralFilter(img,9,75,75)
cv2.imshow("bi_f",bi_f)


cv2.waitKey(0)
cv2.destroyAllWindows()