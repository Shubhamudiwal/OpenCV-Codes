import cv2


"""cap =  cv2.VideoCapture("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\test2.mp4")
print("cap",cap)

while True:
    ret,frame =  cap.read()
    frame = cv2.resize(frame, (700,450))
    gray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#to change colored frame to gray scale
    cv2.imshow("gray",gray)
    cv2.imshow("frame",frame)
    k=cv2.waitKey(25)#25 is used as parameter to play in normal playback speed
    if k== ord("q") & 0xFF:# to terminate a video
        break
cap.release()#release a video
cv2.destroyAllWindows() 
"""


cap =  cv2.VideoCapture(0,cv2.CAP_DSHOW)

#DIVX, XVID,MJPG, X264, WMV1, WMV2
fourcc= cv2.VideoWriter_fourcc(*"XVID")

#It contain 4 parameter, name, codec,fps,resolution
output= cv2.VideoWriter("D:\\outout.avi",fourcc,20.0,(640,480))

while cap.isOpened():
    ret,frame =  cap.read()
    if ret == True:
        #frame = cv2.resize(frame, (700,450))
        gray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#to change colored frame to gray scale
        cv2.imshow("gray",gray)
        cv2.imshow("frame",frame)
        output.write(frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()#release a video
#output.release()
cv2.destroyAllWindows() 