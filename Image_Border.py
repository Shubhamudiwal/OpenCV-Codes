#Creating  Image border--
# With the help of cv2.copyMakeBorder() function.
#it take parameters like(img,border_width(4-sides),bordertype,val_boder)
#border width = top,bottom,right,left







import cv2
import numpy as np
img1= cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\lion.jpg")

#Creating image border
brdr = cv2.copyMakeBorder(img1,10,10,5,5,cv2.BORDER_CONSTANT,value = [255,0,125])
brdr =cv2.resize(brdr,(1000,600))
cv2.imshow("res",brdr)
cv2.waitKey(0)
cv2.destroyAllWindows()