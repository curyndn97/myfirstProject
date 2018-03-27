import numpy as np
import cv2
#import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt


# Load an color image in grayscale
#img = cv2.imread('ArrowL.jpg')
image = cv2.imread("Image.png")


# Tạo một hình ảnh màu đen
img = np.zeros ((512,512,3), np.uint8)
# Vẽ một đường chéo màu xanh với độ dày 5 px
cv2.line (img, (0,0), (511,511), (255,255,255), 5)

# Vẽ một hinh chu nhat
cv2.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Vẽ một hinh tron
cv2.circle(image,(100,100), 63, (0,0,255), -1)

#ronation image
image = cv2.imread("Image.png",1)
rows = image.shape[0]
cols = image.shape[1]
M = cv2.getRotationMatrix2D((cols/2,rows/2),0,2)
image = cv2.warpAffine(image,M,(cols,rows))

cv2.imshow('image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()