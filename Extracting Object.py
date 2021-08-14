#Extracting object from the image and place on another image
#random figure ROI or Background Subtraction.

import cv2
import numpy as np

#Load two images

img1 = cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\hero1.jpg",1)
img2 = cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\strom_breaker.JPG",1)

img1 = cv2.resize(img1,(1024,650))
img2 = cv2.resize(img2,(600,650))

#I Want to fix image 2 data into img1
r,c,ch = img2.shape
print(r,c,ch)

#roi ==

roi = img1[0:r,0:c]

# Now creating mask for img1
img_gry = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)


#create mask using threshold
_,mask = cv2.threshold(img_gry,50,255,cv2.THRESH_BINARY)


##remove back
mask_inv= cv2.bitwise_not(mask)

#put mask into roi
img1_bag= cv2.bitwise_and(roi,roi,mask=mask_inv)

#Take only region of figure from original image.
img2_fg = cv2.bitwise_and(img2,img2,mask=mask)



#Put logo in ROI and modify the main image
res =  cv2.add(img1_bag,img2_fg)

# cv2.imshow("image1",img1)
# cv2.imshow("image2",img2)
# cv2.imshow("ROI",roi)
# cv2.imshow("Step -1 gry ==",img_gry)
# cv2.imshow("Step -2 Mask ==",mask)
# cv2.imshow("Step -3 MaskINV ==",mask_inv)
# cv2.imshow("Step -4 img1_bag ==",img1_bag)
# cv2.imshow("Step -5 img2_fg ==",img2_fg)
# cv2.imshow("Step -6 res ==",res)
final =img1

final [0:r,0:c]=res

cv2.imshow("Step -7 res ==",final)
cv2.waitKey(0)
cv2.destroyAllWindows()
