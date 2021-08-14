#Image Blending with open CV
# Here We use two important functions  cv.add(),cv.addweight
#Blending means addition of two images
#if you want t blend two images then both have same size

import  cv2 as cv
import numpy as np
img1 = cv.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\roi_opr.jpg")
img1 = cv.resize(img1,(500,700))
img2 = cv.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\bro_thor.jpg")
img2 = cv.resize(img2,(500,700))
#cv.imshow("thor==",img1)
#cv.imshow("bro_thor==",img2)
#Now perform blending
#result =  img1+img2
#cv.imshow("result==",result)
# result1= cv.add(img2,img1)#ists your saturated opration which means value to value 
#cv.imshow("result1",result1)


#function cv.addWeighted(img,wt1,img2,wt2,gama_val)
# result2 = cv.addWeighted(img1,0.5,img2,0.5,0)
# cv.imshow("result2",result2)

def blend(x):
    pass

img = np.zeros((400,400,3),np.uint8)
cv.namedWindow('win')
cv.createTrackbar('alpha',"win" , 1, 100, blend)
switch = '0: OFF \n 1 : ON'
cv.createTrackbar(switch,'win',0,1,blend)
while True:
    s =  cv.getTrackbarPos(switch,"win")
    a =  cv.getTrackbarPos("alpha","win")
    n =  float(a/100)
    print(n)
    if s ==0:
        dst = img[:]
    else:
        dst= cv.addWeighted(img1,1-n,img2,n,0)
        cv.putText(dst,str(a),(20,50),cv.FONT_ITALIC,2,(0,125,255),2)
    cv.imshow('dst',dst)
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
cv.waitKey(0)
cv.destroyAllWindows()


