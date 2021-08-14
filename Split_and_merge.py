#Image operation with pixel and cordinates--

import cv2
import numpy as np
""" 
Read an image 
img= cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\pikachu.jpg")
img =cv2.resize(img,(300,400))
print("shape== ",img.shape)#returns a tuple of number of rows,column,chennal
print("no. of pixel== ",img.size)#returns Total number of pixel in a image
print("dataType== ",img.dtype)#returns image datatype
print("Imagetype== ",type(img))
#Now try to split image
#split -  return 3 channel of your image which is blue,green,red
b,g,r = cv2.split(img)


cv2.imshow("blue",b)
cv2.imshow("green",g)
cv2.imshow("red",r)
cv2.imshow("original",img)


"Now if you want to mix the channels then use merge"

mr1 =  cv2.merge((g,b,r))
cv2.imshow("rgb",mr1)
cv2.imshow("original",img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
"""
#Working on pixel color value
img= cv2.imread(r"C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\lion.jpg")
img=cv2.resize(img,(1024,700))
cv2.imshow("lion==",img)
print("shape== ",img.shape)#returns a tuple of number of rows,column,chennal
print("no. of pixel== ",img.size)#returns Total number of pixel in a image
print("dataType== ",img.dtype)#returns image datatype
print("Imagetype== ",type(img))

#access a pixel value by its row and column coordinates.
px= img[520,580]#store cordinate in variable
print("the pixel of that co-ordinates==",px)#We get the pixel.

#Now try to find selected channel value from coordinate
#we know we have three channel - 0,1,2
#accessing only blue pixel
blue=img[520,580,0]
print("the pixel having blue color==",blue)
#accessing only green pixel
green =  img[520,580,1]
print("The pixel having green color==",green)

#accessing only red pixel
red = img[520,580,2]
print("The pixel having red color==",red)


cv2.waitKey(0)
cv2.destroyAllWindows()