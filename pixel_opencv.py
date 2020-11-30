
#this is all trash, no need to keep reading


import numpy as np
import cv2 

def cut_image(event, x, y, flags, params):
    point1 = False
    point2 = False
    rect = (0,0,0,0)
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


img = cv2.imread("6pack_cat.Jpg")
new_img = np.zeros((500,500))
#goi ra 1 pixel tai diem x=500,y=500; gia tri tra ve la [blue,green,red]
'''px = img[500,500]

img[:,:,0] = 125
img[:,:,1] = 125

print(px)
'''
cv2.namedWindow('2')
cv2.setMouseCallback('2',cut_image)
cv2.imshow('2', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
