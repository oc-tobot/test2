import cv2
#get coordinate of the place where mouse click
def get_coor(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
    # Do Whatever you want to, when the event occurs
        ix,iy = x,y
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img, str(ix),(x-100,y),font,1,(255,0,0),4)
        cv2.putText(img, str(iy),(x-100,y+30),font,1,(255,0,0),4)
    

'''cut image on mouse click (like drawing a rectangle) : go to click_and_crop for the right click and crop fucntionality'''
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
            return rect

#resize an image : this is the right one
def resize(new_x,new_y,img):
    global new_img
    new_img = cv2.resize(img, (new_x,new_y))
    return new_img

img = cv2.imread('6pack_cat.jpg')
img2 = cv2.imread('6pack_cut.jpg')
resize(240,240,img2)
cv2.imwrite('6pack_cut_resized.jpg', new_img)
while True:
    cv2.imshow('1',img)
    cv2.imshow('2',img2)
    cv2.imshow('3', new_img)
    k = cv2.waitKey(1) 
    if k == 27:
        break
cv2.destroyAllWindows()