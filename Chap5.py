import cv2
import numpy as np
img = cv2.imread("Resources/Cards.jpg")

width,height = 105,148
pts1 = np.float32([[110,46],[213,68],[80,186],[184,207]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOut = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("Image",img)
cv2.imshow("Output",imgOut)
cv2.waitKey(0)