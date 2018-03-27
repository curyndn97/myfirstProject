import cv2
import numpy as np 

img1 = cv2.imread('avatar.jpg',0)
img2 = cv2.imread('sign3.png',0)

print(img1.shape)
print(img2.shape)
img1 = img1[0:240,0:240]
img2 = img2[240:480,240:480] 
img3 = cv2.add(img1,img2)

cv2.imshow("image1",img1)
cv2.imshow("image2",img2)
cv2.imshow("image3",img3)
cv2.waitKey(0)
cv2.destroyAllWindows()
