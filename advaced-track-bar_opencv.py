#trackbar 
'''advance: paint brush + trackbar to paint different colors (not done yet)'''

import numpy as np
import cv2
# The function attached to the trackbar.
def nothing(x):
    pass
cv2.namedWindow("trackbar exercise")
#creat trackbar
cv2.createTrackbar('B', "trackbar exercise", 0, 255, nothing)
cv2.createTrackbar('G', "trackbar exercise", 0, 255, nothing)
cv2.createTrackbar('R', "trackbar exercise", 0, 255, nothing)
cv2.createTrackbar('Radius', "trackbar exercise", 0, 100, nothing)
#creat switch
switch = '0:OFF\n1:ON'
cv2.createTrackbar(switch, "trackbar exercise", 0, 1, nothing)

#capture mouse event 
drawing = False
mode = True
ix,iy = -1,-1
def on_mouse(event, x,y, flags, params):
    global drawing,ix,iy, mode
    if event == cv2.EVENT_RBUTTONDOWN:
        drawing = True
        ix,iy = x,y
    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.circle(img, (x,y), radius, (b,g,r), 10)
            else:
                cv2.rectangle(img, (ix,iy),(x,y), (b,g,r), 10)
    elif event == cv2.EVENT_RBUTTONUP:
        drawing = False
        if mode == True:
            cv2.circle(img, (x,y), radius, (b,g,r), 10)
        else :
            cv2.rectangle(img, (ix,iy),(x,y), (b,g,r), 10)

#create black image
img = np.zeros((340,500,3), np.uint8)
cv2.namedWindow('trackbar exercise')
cv2.setMouseCallback('trackbar exercise', on_mouse)

while(1):
    cv2.imshow('trackbar exercise', img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break
    elif k == ord(" "):
        mode = not mode
    b= cv2.getTrackbarPos("B","trackbar exercise")
    g= cv2.getTrackbarPos("G","trackbar exercise")
    r= cv2.getTrackbarPos("R","trackbar exercise")
    s= cv2.getTrackbarPos(switch,"trackbar exercise")
    radius= cv2.getTrackbarPos('Radius',"trackbar exercise")

    if s== 0 :
        img[:]=0


cv2.destroyAllWindows()