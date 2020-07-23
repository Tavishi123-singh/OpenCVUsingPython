import cv2
import numpy as np
img = cv2.imread("Resources/AWS.png")
imgResize = cv2.resize(img,(640,480))
imgGray = cv2.cvtColor(imgResize,cv2.COLOR_BGR2GRAY)
imgHor = np.hstack((imgResize,imgResize,imgResize))
imgVer = np.vstack((imgResize,imgResize,imgResize))
grey = cv2.cvtColor(imgResize, cv2.COLOR_BGR2GRAY)
# Make the grey scale image have three channels
grey_3_channel = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)
numpy_horizontal_concat = np.concatenate((imgResize, grey_3_channel,imgResize), axis=1)
numpy_vertical_concat = np.concatenate((imgResize, grey_3_channel,imgResize), axis=0)
cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)
cv2.imshow('Numpy Vertical Concat', numpy_vertical_concat)
#cv2.imshow("Image",img)
#cv2.imshow("Horizontal",imgHor)
#cv2.imshow("Vertical",imgVer)
cv2.waitKey(0)