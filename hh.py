import cv2                             
import numpy as np                           
cap = cv2.VideoCapture("hand.jpg") 
success,img = cap.read() 
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray,(5,5),0)
ret,thresh1 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
#ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
_, contours, _=cv2.findContours(thresh1,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img, contours, -1, (0,255,0), 3)
cv2.imwrite("fram20sec.jpg", thresh1)
cv2.imshow('input',thresh1)                  
cv2.waitKey(30000)

   