import numpy as np 
import cv2


img = cv2.imread('anhtay.jpg',1)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

'''for i in range(hsv.shape[0]):
	for j in range(hsv.shape[1]):
		x = (hsv[i][j][0])
		if x>(0.22*255) and x < (0.45*255) :
			hsv[i][j] = 255
		else :
			hsv[i][j] = 0'''	 

for i in range(gray.shape[0]):
	for j in range(gray.shape[1]):
		if gray[i][j] > 45 :
			gray[i][j] = 255
		else:
			gray[i][j] = 0

kernel = np.ones((17,17),np.float32)
opening = cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)


cv2.imshow('opening',opening)
cv2.imshow('closing',closing)
cv2.waitKey(0)
cv2.destroyAllWindows()