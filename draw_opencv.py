import numpy as np
from cv2 import cv2

img = cv2.imread("DuongThiThuHa.jpeg", 1)
#ve line circle rectangle tren hinh anh
cv2.line(img, (200 ,420),(550,420), (2,2,255),6)
cv2.line(img, (550 ,420),(550,870), (2,2,255),6)
cv2.line(img, (550,870),(200,870), (2,2,255),6)
cv2.line(img, (200,870),(200,420), (2,2,255),6)
cv2.circle(img, (375,645),175,(255,2,2),5)
cv2.rectangle(img,(0,0),(255,255),(2,255,2),7 )
#viet chu len anh
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'DuongThiThuHa', (200,420),font,1,(255,0,0),2)
#Import only if not previously imported
import cv2
# Coordinates must be a tuple - (x,y)
cv2.arrowedLine(img,(300,430),(500,600),(0,0,0),3)                   #Color is by default black

#ve bang cach thay doi mau tung diem trong ma tran 
for i in range(500):
    img[i][i] = (255, 255, 255)
    img[i+2][1+2] = (255, 255, 255)
for i in range(300):
    for j in range(300):
        if img[i,j][0] > 250:
            #ve circle quanh pixel co (b,g,r)>(250,g,r)
            cv2.circle(img, (i,j), 20, (150,252,125),1)
            
cv2.imwrite("daxuly.jpg", img)
img2 = cv2.imread("daxuly.jpg")
cv2.imshow('anh da qua xu ly', img2)
cv2.waitKey(0)

cv2.destroyAllWindows()
