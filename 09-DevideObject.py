import numpy as np
import cv2

#########################################
src = cv2.imread('color.png',1)
src = cv2.resize(src,(600,400),interpolation = cv2.INTER_AREA)

src_hsv =cv2.cvtColor(src,cv2.COLOR_BGR2HSV);

# diện tích của src
frameArea = src.shape[0]*src.shape[1]

#blue color
min_color = np.array([ 97 ,255 ,232])
max_color = np.array([ 100 ,255 ,232])

mask = cv2.inRange(src_hsv,min_color,max_color)

dst = cv2.bitwise_and(src,src,mask = mask)


#tìm biên object
cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
            
largestArea = 0
largestRect = None

if len(cnts) > 0:
        for cnt in cnts:
               
            rect = cv2.minAreaRect(cnt)
            box = cv2.boxPoints(rect)
            box = np.int0(box)
                
            sideOne = np.linalg.norm(box[0]-box[1])
            sideTwo = np.linalg.norm(box[0]-box[3])
            area = sideOne*sideTwo
            if area > largestArea:
                largestArea = area
                largestRect = box
    #Vẽ hình chữ nhật lên đối tượng
if ((largestArea > frameArea*0.001) and (largestArea < frameArea*0.09)):
        cv2.drawContours(src,[largestRect],0,(0,0,255),2)
        print(largestArea,"   :  ",frameArea)  

sub = src-dst
cv2.imshow('sub',sub)
cv2.imshow('dst',dst)
cv2.imshow('src',src)
cv2.waitKey(0)
cv2.destroyAllWindows()            