#In this videom,we talk about ROI(Region of Interest)
import cv2
import numpy as np

#Read the Image
img=cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\roi_opr.jpg")
img= cv2.resize(img,(800,800))

#Region of interest 

#(320,50)
#(440,205)
#[(y1:y2),(x1,x2)]
#y=155,x =120
roi = img[50:205,320:440]

#now passing data into img
img[50:205,431:551]= roi
img[50:205,552:672]= roi
img[50:205,200:320]=roi
img[50:205,80:200]=roi

#Ironman

img1=cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\ironman.jpg")
img1=cv2.resize(img1,(900,600))
img1[1:156,560:680]=roi
cv2.imshow("res",img1)
cv2.waitKey(0)
cv2.destroyAllWindows()