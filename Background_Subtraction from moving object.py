#Background subtraction is a way to access the foreground objects.

#Technically, you need to extract the moving
#foreground from static background.
#There are multiple approach for background subtraction.
#We discuss all of them.

import numpy as np
import cv2 
cap = cv2.VideoCapture("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\test2 - Copy.mp4")

#old alg = cv2.basegm.createBackgroundSubtractorMOG()
algo1= cv2.createBackgroundSubtractorMOG2(detectShadows=True)#algo1
algo2= cv2.createBackgroundSubtractorKNN(detectShadows=True)#algo2
while  True:
    ret,frame = cap.read()
    frame =cv2.resize(frame,(600,400))
    if frame is None:
        break
    res1 = algo1.apply(frame)
    res2 = algo2.apply(frame)
    
    cv2.imshow("Original", frame)
    cv2.imshow("res1", res1) 
    cv2.imshow("res2", res2)
    
    k = cv2.waitKey(60)
    if k == "q" or k== 27:
        break
    
cap.release()
cv2.destroyAllWindows()