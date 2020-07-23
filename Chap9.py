import cv2
import numpy as np
faceCascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("Resources/sampleImage.jpg")
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(imgGray,1.1,4)
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
    cv2.rectangle(imgGray, (x, y), (x + w, y + h), (0, 0, 255), 2)
cv2.imshow("Image",img)
cv2.imshow("Gray Image",imgGray)
cv2.waitKey(0)