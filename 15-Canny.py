import numpy as np 
import cv2
from matplotlib import pyplot as plt

src_1 = cv2.imread('anhtay.jpg',1)
src_2 = cv2.imread('3.jpg',1)
'''src_3 = np.zeros(((src_1.shape[0]),src_1.shape[1]+src_2.shape[1],3),np.float32)
print(src_3.shape[0],'  ',src_3.shape[1])
for i in range(src_1.shape[0]):
	for j in range(src_1.shape[1]):
		src_3[i][j][0] = src_2[i][j][0]
		src_3[i][j][1] = src_2[i][j][1]
		src_3[i][j][2] = src_2[i][j][2]
		src_3[i][j+src_2.shape[0]][0] = src_1[i][j][0]
		src_3[i][j+src_2.shape[0]][1] = src_1[i][j][1]
		src_3[i][j+src_2.shape[0]][2] = src_1[i][j][2]'''

dst = cv2.GaussianBlur(src_1,(5,5),0)
dst = cv2.Canny(src_1,150,255)


cv2.imshow('Image',dst)
#cv2.imshow('Image2',src_3)
cv2.waitKey(0)
cv2.destroyAllWindows()