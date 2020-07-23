import cv2
img = cv2.imread("Resources/Lambo.jpg")
print(img.shape)

imgResize = cv2.resize(img,(640,480))
print(imgResize.shape)

imgCrop = img[0:100,150:200]
cv2.imshow("Image",img)
cv2.imshow("Image Resize",imgResize)
cv2.imshow("Image Cropped",imgCrop)
cv2.waitKey(0)