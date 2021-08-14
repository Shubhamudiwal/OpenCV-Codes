import cv2
import numpy as np

#img =  cv2.imread(r"C:\Users\DELL\Desktop\OpenCv\Image-Processing-Tutorials-main\Data\thor.jpg")
#img = cv2.resize(img,(600,700))

#Black Image
#img=np.zeros([512,512,3],np.uint8)*255

#White Image
img=np.ones([512,512,3],np.uint8)*255
#Here line accept 5 parameter (img,strating,ending,color,thickness)
img= cv2.line(img,(0,0),(200,200),(154,92,424),5)# Python follow BGR colour code

#Arriwed line accept 5 parameter (img,strating,ending,color,thickness)
img= cv2.arrowedLine(img,(0,125),(255,255),(255,0,125),10)# Python follow BGR colour code

#Rectangle - accept parameter(img,start_co,end_co, color,thickness)
img=cv2.rectangle(img,(384,10),(510,128),(128,0,255),8)#Hollow rectangle

#Rectangle - accept parameter(img,start_co,end_co, color,thickness)
#img=cv2.rectangle(img,(384,10),(510,128),(128,0,255),-1)#Filled rectangle

#Circle - accept(img,star_co,radius,color,thichness)
#img=cv2.circle(img,(447,125),63,(214,255,0),-5)#Filled Circle

#Circle - accept(img,star_co,radius,color,thichness)
img=cv2.circle(img,(447,125),63,(214,255,0),5)#Hollow circle

#puttext

font = cv2.FONT_HERSHEY_COMPLEX
#puttext - accept(img,text,start_co,font, fontsize,color,thickness,linetype)

img= cv2.putText(img,"THOR",(20,500),font,2,(0,125,255),5,cv2.LINE_AA)

#ellipse-accept(img,start_cor,(Length,height),color,thickness)
img=cv2.ellipse(img,(400,600),(100,50),0,0,360,155,5)

cv2.imshow("res",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
