import cv2
#print("Package imported")
imgA = cv2.imread("Resources/AWS.png")
cv2.imshow("AWS Logo",imgA)
#cap = cv2.VideoCapture("Resources\NeonZji.mp4")
cam = cv2.VideoCapture(0)
cam.set(3,640)
cam.set(4,480)
cam.set(10,100)
#cv2.imshow("Output",img)
#cv2.waitKey(0)
while True:
    #success,imgV = cap.read()
    suc, imgC = cam.read()
    #cv2.imshow("Video",imgV)
    cv2.imshow("WebCam", imgC)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break