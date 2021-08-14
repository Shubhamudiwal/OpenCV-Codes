
import cv2
import pafy

url="https://www.youtube.com/watch?v=JTuNbrs1cZ0"
 
"""data = pafy.new(url)

data=data.getbest(preftype = "mp4")
cap =  cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(data.url)


#DIVX, XVID,MJPG, X264, WMV1, WMV2
fourcc= cv2.VideoWriter_fourcc(*"XVID")

#It contain 4 parameter, name, codec,fps,resolution
output= cv2.VideoWriter("D:\\outout.mp4",fourcc,20.0,(640,480))
print("Check===",cap.isOpened())

while cap.isOpened():
    ret,frame =  cap.read()
    if ret == True:
        frame = cv2.resize(frame, (700,700))
        gray =  cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)#to change colored frame to gray scale
        #cv2.imshow("gray",gray)
        #cv2.imshow("Colorframe",frame)
        output.write(frame)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
cap.release()#release a video
output.release()
cv2.destroyAllWindows() """
video = pafy.new(url)
best  = video.getbest(preftype="mp4")
capture = cv2.VideoCapture(best.url)
fourcc= cv2.VideoWriter_fourcc(*"XVID")
output= cv2.VideoWriter("D:\\outout.mp4",fourcc,20.0,(640,480))
while True:
    check, frame = capture.read()
    #print (check, frame)
    cv2.imshow('frame',frame)
    output.write(frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
            break
capture.release()
output.release()
cv2.destroyAllWindows()
