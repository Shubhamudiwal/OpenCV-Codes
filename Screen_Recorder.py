#Screen Recorder

import cv2
import pyautogui as p
import numpy as np

#Create resolution
"""rs = p.size()

#filename in which we store recording
fn= input("Please Enter any file name and Path")
#Fix the frmae rate

fps = 20.0

fourcc = c.VideoWriter_fourcc(*'XVID')
output = c.VideoWriter(fn,fourcc,fps,rs)


c.namedWindow("Live_Recording",c.WINDOW_NORMAL)
c.resizeWindow("Live_Recording",(600,400))

while True:
    img = p.screenshot()
    f = np.array(img)
    f= c.cvtColor(f,c.COLOR_BGR2RGB)
    output.write(f)
    c.imshow("Live_recording",f)
    if c.waitKey(1)== ord("q"):
        break
  
#c.release()
output.release()
c.destroyAllWindows()"""

#Break Video into multiple images and store in a folder
vidcap = cv2.VideoCapture(r"C:\Users\DELL\Desktop\OpenCv\Image-Processing-Tutorials-main\Data\test2.mp4")
ret,image= vidcap.read()
count = 0
while True:
    if ret==True:
        cv2.imwrite("D:\\imgN%d.jpg"%count,image)
        vidcap.set(cv2.CAP_PROP_POS_MSEC,(count**100))
        ret,image = vidcap.read()
        cv2.imshow("res",image)
        count +=1
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
            cv2.destroyAllWindows()
            
vidcap.release()
cv2.destroyAllWindows()