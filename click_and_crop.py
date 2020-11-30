#click and crop image da lam xong
#click and crop video chua xong

import cv2

point = []
croping = False
def click_crop(event, x, y, flags, params):
    global point, croping
    # capture the first point 
    if event == cv2.EVENT_RBUTTONDOWN:
        point = [(x,y)]
        croping = True
    #capture the second point, require dragging the mouse to the second point
    elif event == cv2.EVENT_RBUTTONUP:
        point.append((x,y))
        croping = False
        
        #draw a rectangle around the area of the image being cropped (when drawing in video, this wont work, have to call the function inside "while(cap.isopened())")
        cv2.rectangle(frame, point[0],point[1], (0,255,0),2)
        


''' click and crop image
img = cv2.imread('6pack_cat.jpg', 1)
clone = img.copy()
cv2.namedWindow('image display')
cv2.setMouseCallback('image display', click_crop)
'''
#click and crop video
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
frame = cv2.flip(frame,1)
clone = frame.copy()
'''while True:
    cv2.imshow('image display', img)
    k = cv2.waitKey(1) & 0xff
    #press space bar to crop the choosen image 
    if k == ord(" "):
        img = clone.copy()
        break
'''
while (cap.isOpened()): #van chua lam xong
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame', click_crop)
    if len(point) == 2:
        cv2.rectangle(frame, point[0], point[1],(0,255,0) , 2)
    cv2.imshow('frame', frame)
    k = cv2.waitKey(1) & 0xff
    if k == ord("c"):
        break
    if len(point) == 2 :
        roi = frame[point[0][1]:point[1][1], point[0][0]:point[1][0]]
        cv2.imshow('region of interest', roi)

cap.release()
cv2.destroyAllWindows()