#test of measuring performance
import numpy as np
import cv2 as cv
'''
img1 = cv.imread('6pack_cut.jpg')
img = cv.cvtColor(img1,cv.COLOR_BGR2HSV)
e1 = cv.getTickCount()
cv.imshow('s', img)
e2 = cv.getTickCount()
t = (e2 - e1)/cv.getTickFrequency()
print( t )
cv.imshow('1',img1)
cv.waitKey(0)
cv.destroyAllWindows()
'''
cap = cv.VideoCapture(0)
ret, frame = cap.read()
hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
lower_blue = np.array([110,50,50], np.uint8)
higher_blue = np.array([130,255,255], np.uint8)
while(1):

    cv.imshow('1',hsv)
    cv.imshow('2', lower_blue)
    cv.imshow('3', higher_blue)
    if cv.waitKey(1) &0xff == 27:
        break
cv.destroyAllWindows()