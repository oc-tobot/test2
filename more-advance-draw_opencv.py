import cv2 as cv
import numpy as np

drawing = False
mode = True #true then draw rectangle, else draw circle
ix,iy = -1,-1

def on_mouse(event, x,y,flags, param):
    global ix, iy, drawing, mode

    if event == cv.EVENT_LBUTTONDOWN:
        drawing = True
        ix, iy = x,y
    elif event == cv.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv.rectangle(frame, (ix,iy), (x,y), (0,255,0), -1)               
            else :  
                cv.circle(frame, (x,y), 10, (0,0,255), -1)
    elif event == cv.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv.rectangle(frame, (ix,iy), (x,y), (0,0,255), -1)
        else :
            cv.circle(frame, (x,y), 10, (0,255,0), -1)

frame = np.zeros((640,480,3), np.uint8)
cv.namedWindow('frame')
cv.setMouseCallback('frame', on_mouse)

while(1):
    cv.imshow('frame', frame)
    k = cv.waitKey(1) & 0xFF
    if k == ord(" "):
        mode = not mode
    elif k == 27:
        break

cv.destroyAllWindows()