import cv2#Opencv library import and it is used as cv2 in python


'''img1= cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\avengers.jpg",1)
img1= cv2.resize(img1,(1280,700))# width,height
print(img1)
cv2.imshow("original",img1)


#Greyscale image
img2= cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\avengers.jpg",0)
img2= cv2.resize(img2,(1280,700))# width,height
print("Image in grey scale == \n",img2)
cv2.imshow("Grey Scale Image",img2)

#Unchanged image
img3= cv2.imread("C:\\Users\\DELL\\Desktop\\OpenCv\\Image-Processing-Tutorials-main\\Data\\avengers.jpg",-1)
img3= cv2.resize(img3,(1280,700))# width,height
print("Image in unchanged mode == \n",img3)
cv2.imshow("Uncahnged",img3)


cv2.waitKey()
cv2.destroyAllWindows()'''

path= input("Enter the Path and name of an image===")
print("You Enter this===",path)
img1=cv2.imread(path,0)
img1 = cv2.resize(img1,(560,700))
img1 = cv2.flip(img1,-1)
print(img1)
cv2.imshow("converted image ==",img1)
cv2.waitKey()
cv2.destroyAllWindows()

'''k=cv2.waitKey()
if k ==ord("s"):
    cv2.imwrite("D:\\output.png",img1)
else:
    cv2.destroyAllWindows()'''
