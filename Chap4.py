import cv2
import numpy as np
img = np.zeros((512,512,3),np.uint8)
#img[:] = 255,0,0
cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),1)
#cv2.rectangle(img,(0,0),(200,300),(0,0,255),cv2.FILLED)
cv2.rectangle(img,(0,0),(200,300),(0,0,255),3)
cv2.circle(img,(300,400),50,(150,0,0),5)
cv2.putText(img,"OPENCV",(200,300),cv2.FONT_ITALIC,1,(0,100,0),5)
print(img.shape)
cv2.imshow("Image",img)
cv2.waitKey(0)