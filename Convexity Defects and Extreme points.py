import cv2
import numpy as np

img = cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\hand1.jpg")
img =cv2.resize(img,(600,700))
img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


#Blur to the rest of image to remove the error 
blur = cv2.medianBlur(img1,9)

#Find threshold
ret,thresh = cv2.threshold(blur,240,255,cv2.THRESH_BINARY_INV)

#Draw contour
cnts,hier =  cv2.findContours(thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#cv2.drawContours(img,cnts,-1,(50,50,150),2)

#Here cnts is a list of contours, and each contour is an array with x and y
#hier variable called hierarchy and it contain image information.

print("Number of contour==",cnts,"\ntotal contour==",len(cnts))
print('Hierarchy==\n',hier)



#Loop over the contours

for c in cnts:
    epsilon = 0.0001*cv2.arcLength(c,True)
    data=cv2.approxPolyDP(c,epsilon,True)
    
    hull = cv2.convexHull(data)
    cv2.drawContours(img,[c],-1,(50,50,150),2)
    cv2.drawContours(img,[hull],-1,(0,255,0),2)
 
#find convexity defect
hull2 = cv2.convexHull(cnts[0],returnPoints =False)
#defects return an array which contain value [start_point,end_point]
defect = cv2.convexityDefects(cnts[0],hull2)

for i in range(defect.shape[0]):
    s,e,f,d = defect [i,0]
    print(s,e,f,d)
    start = tuple(c[s][0])
    end =  tuple(c[e][0])
    far = tuple(c[f][0])
    #cv2.line(img,start,end,[255,0,0],2)
    cv2.circle(img,far,5,[0,0,255],-1)
                  

#Extreme Points
#It means topmost, bottommost, rightmost and leftmost point

c_max = max(cnts, key= cv2.contourArea)

#determine the most extreme points along the contour

extleft = tuple(c_max[c_max[:,:,0].argmin()][0]) 
extRight = tuple(c_max[c_max[:,:,0].argmax()][0])   
extTop = tuple(c_max[c_max[:,:,1].argmin()][0]) 
extBot = tuple(c_max[c_max[:,:,1].argmax()][0]) 


#draw the outline of the object, then draw each of the
#extreme points, where the left-most is red,right most
#is green, top-most is blue , and bottom most is teal


cv2.circle(img,extleft,8,(255,0,255),-1)#pink
cv2.circle(img,extRight,8,(0,125,255),-1)#Brown
cv2.circle(img,extTop,8,(255,10,0),-1)#Blue
cv2.circle(img,extBot,8,(19,152,152),-1)#green




cv2.imshow("original",img)
cv2.imshow("Gray == ",img1)
cv2.imshow("Threshold",thresh)

cv2.waitKey(0)
cv2.destroyAllWindows()
