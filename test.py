
#test: draw circle on black image
'''
#Import only if not previously imported
import numpy as np
import cv2 as cv
def draw_circle(event, x, y, flags, param):
    if event == cv.EVENT_RBUTTONUP:
        cv.circle(img, (x,y),60,(255,255,255),1)
img = np.zeros((680,680,3), np.uint8)
cv.namedWindow("Mouse Event test")
cv.setMouseCallback("Mouse Event test", draw_circle)
# Attach a image (On which you want to handle the event) to the same window (Window Name).

while(1):
    cv.imshow("Mouse Event test", img)
    if (cv.waitKey(20) & 0xFF == 27):
        break   

cv.destroyAllWindows()
'''
#test: calculate the radius
'''
temp1 = [15,20]
temp2 = [10,15]
temp3 = [temp1[0] - temp2[0],temp1[1]-temp2[1]]
print (((temp3[0])**2+(temp3[1])**2)**0.5)
'''
#test: draw rectangle on two mouse click (not double click)
'''
import numpy as np
import cv2

rect = (0,0,0,0)
startPoint = False
endPoint = False

def on_mouse(event,x,y,flags,params):

    global rect,startPoint,endPoint

    # get mouse click
    if event == cv2.EVENT_LBUTTONDOWN:

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

cap = cv2.VideoCapture(0)
waitTime = 50

#Reading the first frame
(grabbed, frame) = cap.read()

while(cap.isOpened()):

    (grabbed, frame) = cap.read()

    cv2.namedWindow('frame')
    cv2.setMouseCallback('frame', on_mouse)    

    #drawing rectangle
    if startPoint == True and endPoint == True:
        cv2.rectangle(frame, (rect[0], rect[1]), (rect[2], rect[3]), (255, 0, 255), 2)

    cv2.imshow('frame',frame)

    key = cv2.waitKey(waitTime) 

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

#test: drawing the boder of the rectangle 
import cv2
# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
refPt = (0,0,0,0)
cropping = False
def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping
    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = (x,y,0,0)
        cropping = True
    # check to see if the left mouse button was released
    elif event == cv2.EVENT_LBUTTONUP:
        # record the ending (x, y) coordinates and indicate that
        # the cropping operation is finished
        refPt = (refPt[0], refPt[1], x,y)
        cropping = False
        # draw a rectangle around the region of interest        
        cv2.rectangle(image, (refPt[0], refPt[1]),(refPt[2],refPt[3]), (255,0,0), 1)
        refPt=(0,0,0,0)

image = cv2.imread("6pack_cat.jpg")
while(1):
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_crop)
    cv2.imshow("image", image)
    if  cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

import numpy as np
import cv2 

point1 = False
point2 = False
rect = (0,0,0,0)

def cut_image(event, x, y, flags, params):
    global rect, point1, point2
    if event == cv2.EVENT_LBUTTONDOWN:
        if point1 == True and point2 == True:
            point1 = False
            point2 = False
            rect = (0,0,0,0)
        elif point1 == False:
            rect = (x,y,0,0,)
            point1 = True
        elif point2 == False:
            rect = (rect[0],rect[1], x, y)
            point2 = True

def get_coor(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
    # Do Whatever you want to, when the event occurs
        ix,iy = x,y
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(ix),(x-100,y),font,1,(255,0,0),4)
        cv2.putText(img, str(iy),(x-100,y+30),font,1,(255,0,0),4)


img = cv2.imread("6pack_cat.Jpg")
new_img = []

#goi ra 1 pixel tai diem x=500,y=500; gia tri tra ve la [blue,green,red]
px = img[500,500]

img[:,:,0] = 125
img[:,:,1] = 125

print(px)

cv2.namedWindow('2')
cv2.setMouseCallback('2',cut_image)
if point1 == True and point2 == True:
    new_img = img[rect[0]:rect[2], rect[1]:rect[3]]
while(1):

    cv2.imshow('2', new_img)
    k = cv2.waitKey(1) 
    if k == 27:
        break

cv2.destroyAllWindows()
'''
import cv2
import numpy as np
img = cv2.imread('6pack_cut.jpg')

b = img[:,:,0]
g = img[:,:,1]
r = img[:,:,2]

a = cv2.merge((g,b,r))
c = cv2.merge((r,b,g))
d = cv2.merge((r,b,b))
x,y= 123,342
#print(a[x,y])
#print(b[x,y])
#print(g[x,y])
#print(a.shape)
cv2.imshow('a',a)
cv2.imshow('c',c)
cv2.imshow('d',d)
cv2.waitKey(0)
cv2.destroyAllWindows()