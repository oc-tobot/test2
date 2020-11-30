import cv2

#read image, and draw
#img = cv2.imread('6pack_cat.jpg',0)
img = cv2.imread('6pack_cat.jpg',1)
#img = cv2.imread('6pack_cat.jpg')
#img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.rectangle(img, (250,250), (500,500),(0,255,0))
cv2.circle(img, (300,300), 50,(255,0,0))
cv2.line(img,(350,350),(550,500),(0,0,255))
cv2.putText(img, ' text', (0,320), cv2.FONT_HERSHEY_SIMPLEX, 2,(0,0,0))
cv2.imshow('display image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''
#streaming video
cap = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*"XVID")
#output = cv2.VideoWriter('output.mp4', fourcc, 20, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
while(1):
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    cv2.imshow('streaming video', frame)
    #output.write(frame)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()'''
'''
#mouse event
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img,(x,y),100,(255,0,0),5)
img = cv2.imread('6pack_cat.jpg')
cv2.namedWindow("mouse event example")
cv2.setMouseCallback("mouse event example", mouse_event)
while(1):
    
    cv2.imshow('mouse event example',img)
    if cv2.waitKey(20) & 0xff == 27:
        break
cv2.destroyAllWindows()
'''

