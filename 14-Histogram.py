import numpy as np
import cv2

#Cân bằng histogram với ảnh màu
def HistogramColor(img):
	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
	#Tách thành 3 kênh màu
	hsv_channel = cv2.split(hsv)

	#Cân bằng histogram
	hsv_channel = cv2.equalizeHist(hsv_channel[2],hsv_channel[2])

	#Trộn ảnh
	cv2.merge(hsv_channel,hsv)

	#Chuyển ảnh về lại BGR để hiển thị
	result = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
	return result

img = cv2.imread('Image.png',1)
img = HistogramColor(img)
cv2.imshow('Histogram Color',img)	

#Cân bằng histogram với ảnh xám
def HistogramGray(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.equalizeHist(gray)
	return gray


img = cv2.imread('Image.png',1)
img = HistogramColor(img)
cv2.imshow('Ảnh màu khi cân bằng Histogram',img)

img = cv2.imread('Image.png',1)
img = HistogramGray(img)
cv2.imshow('Ảnh xám khi cân bằng Histogram',img)

cv2.waitKey(0)
cv2.destroyAllWindows()
