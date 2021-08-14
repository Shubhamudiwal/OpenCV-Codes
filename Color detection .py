#detect color in image

import cv2
import numpy as np

frame =  cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\color_balls.jpg")

while True:
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    u_v =  np.array([48,255,248])
    l_v = np.array([20,143,139])
    
    #creating mask
    mask = cv2.inRange(hsv,l_v,u_v)
    
    #filter mask with image
    
    res = cv2.bitwise_and(frame,frame,mask=mask)
    
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    
    key =cv2.waitKey(1)
    if key == 27:
        break



cv2.waitKey(0)    
cv2.destroyWindows()