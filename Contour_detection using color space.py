#Contour detction using color space
import cv2
import numpy as np

#Read Camera 
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
def nothing(x):
    pass

#window name
cv2.namedWindow("Color Adjustments",cv2.WINDOW_NORMAL)
cv2.resizeWindow("Color Adjustments",(300,300))
cv2.createTrackbar("Thresh","Color Adjustments",0,255,nothing)

#Color Detection Track

cv2.createTrackbar("Lower_H","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_S","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Lower_V","Color Adjustments",0,255,nothing)
cv2.createTrackbar("Upper_H","Color Adjustments",255,255,nothing)
cv2.createTrackbar("Upper_S","Color Adjustments",255,255,nothing)
cv2.createTrackbar("Upper_V","Color Adjustments",255,255,nothing)

while True:
    _,frame = cap.read()
    frame = cv2.resize(frame,(400,400))
    hsv = cv2.cvtColor(frmae, cv2.COLOR_BGR2HSV)
    #detection hand
    l_h = cv2.getTrackbar("Lower_H","Color Adjustments")
    l_s = cv2.getTrackbar("Lower_S","Color Adjustments")
    l_v = cv2.getTrackbar("Lower_V","Color Adjustments")
    
    u_h = cv2.getTrackbar("Upper_H","Color Adjustments")
    u_s = cv2.getTrackbar("Upper_S","Color Adjustments")
    u_v = cv2.getTrackbar("Upper_V","Color Adjustments")
    
    lower_bond = np.array([l_h,l_s,l_v])
    upper_bond = np.array([u_h,u_s,u_v])
    
    #Creating Mask
    mask =  cv2.inRange(hsv,lower_bond,upper_bond)
    
    #filter mask with image
    
    filtr = cv2.bitwise_and(frame,frame,mask =mask)
    
    mask1= cv2.bitwise_not(mask)
    m_g = cv2.getTrackbarPos('Thresh',"Color Adjustments")
    ret,thresh = cv2.threshold(mask1,m_g,255,cv2.THRESH_BINARY)
    dilata = cv2.dilate(thresh,(1,1),iterations = 6)
    
    #findcontour(img, contour_retrival_mode,method)
    cnts,hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #Here cnts is a list of contours.And each contour is an array with x,y cordinate
    #print ("Number of contour==",cnts,"\ntotal contour ==",len(cnts) )
    #print("Hierarchy == \n",hier)
    
    
     #Draw the contours
    #frame= cv2.drawContours(frame,cnts,-1,(176,10,15),4)
    
    # loop over the contours
    
    for c in cnts:
        epsilon = 0.0001*cv2.arcLength(c,True)
        data= cv2.approxPolyDP(c,epsilon,True)
    
        hull = cv2.convexHull(data)
        cv2.drawContours(frame, [c], -1, (50, 50, 150), 2)
        cv2.drawContours(frame, [hull], -1, (0, 255, 0), 2)
        """
        hull = cv2.convexHull(data,returnPoints = False)
        defect = cv2.convexityDefects(data[0],hull)
        print("defect==",defect)
        """
    cv2.imshow("Thresh", thresh)
    cv2.imshow("mask==",mask)
    cv2.imshow("filter==",filtr)
    cv2.imshow("Result", frame)

    key = cv2.waitKey(25) &0xFF
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()