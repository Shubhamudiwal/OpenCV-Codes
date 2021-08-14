#Image histogram - Find, Plot and Analyze
#It which gives you an overall idea about the intensity distribution of an image.
#It distribute data along x and y axis.
#x - axis contain range of color values.
#y- axis contain numbers of pixels in an image.
#With histogram to extract information about constant, brightness and intensity etc.
#Plot histogram using matplotlib


import cv2
import numpy as np

from matplotlib import pyplot as plt

#plotting with calhist method
"""
img = np.zeros((200,200),np.uint8)
cv2.rectangle(img,(0,100),(200,200),(255),-1)
cv2.rectangle(img,(0,50),(50,100),(127),-1)


#It accept parametes like ([img],[channel],mask,[histsize],range)
hist = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(hist)
plt.show()

cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()

"""

#With color image--
img= cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\thor.jpg")
img = cv2.resize(img,(500,600))
"""
b,g,r = cv2.split(img)

cv2.imshow("img",img)
cv2.imshow("b",b)
cv2.imshow("g",g)
cv2.imshow("r",r)

#Plotting different channel with hist
plt.hist(b.ravel(),256,[0,256])
plt.hist(g.ravel(),256,[0,256])
plt.hist(r.ravel(),256,[0,256])

plt.title("ColorFull Image")
plt.show()

"""

#Gray scale
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

"""
hist = cv2.calcHist([img_gray],[0],None,[256],[0,256])
plt.plot(hist)
plt.title("Gray Image")
plt.show()
cv2.imshow("Gray Image",img_gray)

"""



#Histogram equalization is good when of the image is confined to a particular region

"""
#It accept gray scale imge
equ=cv2.equalizeHist(img_gray)
res = np.hstack((img_gray,equ))
cv2.imshow("equ",equ)
hist1 = cv2.calcHist([equ],[0],None,[256],[0,256])
plt.plot(hist1)
plt.title("Equalization")
plt.show()

"""

#CLAHE(Contrast Limited Adaptive Histogram Equalization)
#create a CLAHE object(Arguments are optional.)
#It is used to enhance image and also handle noise from image range
#gray scale image is required
clahe = cv2.createCLAHE(clipLimit = 2.0,tileGridSize = (8,8))
cl1 = clahe.apply(img_gray)
cv2.imshow("clahe",cl1)
hist2 = cv2.calcHist([cl1],[0],None,[256],[0,256])
plt.plot(hist2)
plt.title("CLAHE")
plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()





