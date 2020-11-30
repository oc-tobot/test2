#capture video in real time
#draw circle in real time on mouse click, free size
#draw rectangle in real time on click, free size

#Import only if not previously imported
import cv2 as cv
import numpy as np

circle = (0,0,0,0)
centerPoint = False
radius = 20 
firstPoint = False
secondPoint = False
rect = (0,0,0,0)
startPoint = False
endPoint = False

#get coordinate on mouse click x,y
def on_mouse1(event,x,y,flags,param):
    global circle,centerPoint
    if event == cv.EVENT_LBUTTONDOWN:
        if centerPoint == True:
            circle = (0,0,0,0)
            centerPoint = False
        if centerPoint == False:
            circle = (x,y,0,0)
            centerPoint = True

#get two coordinates, first one is the center and the 2nd is to calculate the radius
def on_mouse2(event,x,y,flags,param):
    global  circle,radius, firstPoint, secondPoint
    if event == cv.EVENT_RBUTTONDOWN:
        if firstPoint == True and secondPoint == True:           
            firstPoint = False
            secondPoint = False
            circle = (0,0,0,0)
        if firstPoint == False :
            circle = (x,y,0,0)
            firstPoint = True
        elif secondPoint == False :
            circle = (circle[0], circle[1],x,y)
            secondPoint = True
        radius = round(((circle[2]-circle[0])**2 + (circle[3]-circle[1])**2)**0.5)

#get two coordinates to dra the rectangle
def on_mouse3(event,x,y,flags,params):    
    global rect,startPoint,endPoint
    # get mouse click
    if event == cv.EVENT_LBUTTONDOWN:
        if startPoint == True and endPoint == True:
            startPoint = False
            endPoint = False
            rect = (0, 0, 0, 0)
        if startPoint == False:
            rect = (x, y, 0, 0)
            startPoint = True
        elif endPoint == False:
            rect = (rect[0], rect[1], x, y)
            endPoint = True

# 0 to capture video on real time
# "video name" to read video
cap = cv.VideoCapture(0)
waittime = 20
#read the first frame
ret, frame = cap.read()
while(cap.isOpened()):
    #cap.read() return true/false (ret is true or false, frame is the image)
    ret, frame = cap.read()
    frame = cv.flip(frame,1)
    # Display the resulting frame
    cv.namedWindow('Frame')
    cv.setMouseCallback('Frame', on_mouse3)
    #drawing circle
    if startPoint == True and endPoint == True:
        cv.rectangle(frame, (rect[0],rect[1]), (rect[2],rect[3]), (255,0,0), 1)
    cv.imshow('Frame', frame)
    #Press esc to close
    key = cv.waitKey(waittime)
    if key == 27:
        break

cap.release()
cv.destroyAllWindows()