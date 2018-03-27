import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('avatar.jpg',0)
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		if img[i][j] <120:
			img[i][j] = 0
		if img[i][j] >120:
			img[i][j] = 255	




'''print (int(img.shape[1]/2),"  ",int(img.shape[0]/2))
pixel = img[int(img.shape[1]/2)][int(img.shape[0]/2)]'''
#print (pixel)
'''print (img.size)
#print (img.dtype)

print (img[150][150])
print (img[150][150][0])

#proccesor pixel
for i in range(img.shape[0]):
	for j in range(img.shape[1]):
		#img[i][j] = [0,255,255]
		if img[i,j,0] > 30:
			img[i,j,0] = 0
			img[i,j,1] = 255
			img[i,j,2] = 0'''
#slit image
'''subimg = img[0:120,0:120]
subimg = subimg[:,:,0]'''

cv2.imshow('image',img)
cv2.imwrite('./FileResult/messi.png',img)
#cv2.imshow('subimg',subimg)
cv2.waitKey(0)
cv2.destroyAllWindows()

