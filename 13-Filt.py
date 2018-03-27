import cv2
import numpy as np
from matplotlib import pyplot as plt

###Bộ lọc Gaussian
#### Bộ lọc Median
#### Bộ lọc Bilateral
#### Bộ lọc FFT
#### Bộ lọc. Sobel '''

###########2D Convolution ( Image Filtering )
def filter2D(img):
	kernel = np.ones((5,5),np.float32)/25
	dst = cv2.filter2D(img,-1,kernel)
	return dst

'''img = cv2.imread('Image.png')
img = filter2D(img)	
cv2.imshow("Filter2D",img)'''

########### Averaging : lọc trung bình
def filterBlur(img):
	blur = cv2.blur(img,(5,5))
	return blur 

'''img = cv2.imread('Image.png')
img = filterBlur(img)	
cv2.imshow("FilterBlur",img)'''

########### Median : lọc trung vị
def filterMedian(img):
	kernel = np.ones((5,5),np.float32)/25
	median = cv2.medianBlur(img,3,kernel)
	return median

'''img = cv2.imread('Opencv-image.png')
img = filterMedian(img)	
cv2.imshow("FilterMedian",img)'''

########### Gaussian : bộ lọc thông cao
def filterGaussianBlur(img):
	blur = cv2.GaussianBlur(img,(5,5),0)
	return blur

'''src = cv2.imread('Opencv-image.png')
dst = filterMedian(src)	
cv2.imshow("filterGaussianBlur",dst)'''


###########Cân bằng histogram với ảnh màu
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

'''img = cv2.imread('Image.png',1)
img = HistogramColor(img)
cv2.imshow('Ảnh màu khi cân bằng Histogram',img)'''

###########Cân bằng histogram với ảnh xám
def HistogramGray(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = cv2.equalizeHist(gray)
	return gray	

'''img = cv2.imread('Image.png',1)
img = HistogramGray(img)
cv2.imshow('Ảnh xám khi cân bằng Histogram',img)'''	

###########Tìm cạnh biên Canny
def Canny(img):
	dst = cv2.GaussianBlur(img,(5,5),0)
	dst = cv2.Canny(img,150,255)
	return dst	

src1 = cv2.imread('Image.png',1)
dst1 = Canny(src1)
cv2.imshow('Image',src1)


'''plt.subplot (121), plt.imshow (src1), plt.title ( 'Bản gốc' )
plt.xticks ([]), plt.yticks ([])
plt.subplot (122), plt.imshow (dst1), plt.title ( 'Bản qua xử lí' )
plt.xticks ([]), plt.yticks ([])
plt.show ()'''


cv2.waitKey(0)
cv2.destroyAllWindows()


'''kernel[0][0] = 6
kernel[0][1] = 6
kernel[0][2] = 6
kernel[0][3] = 6
kernel[0][4] = 6
kernel[1][0] = 6
kernel[1][1] = 6
kernel[1][2] = 6
kernel[1][3] = 6
kernel[1][4] = 6
kernel[2][0] = 6
kernel[2][1] = 6
kernel[2][2] = 6
kernel[2][3] = 6
kernel[2][4] = 6
kernel[3][0] = 6
kernel[3][1] = 6
kernel[3][2] = 6
kernel[3][3] = 6
kernel[3][4] = 6
kernel[4][0] = 6
kernel[4][1] = 6
kernel[4][2] = 6
kernel[4][3] = 6
kernel[4][4] = 6'''