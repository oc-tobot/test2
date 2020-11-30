'''
#Import only if not previously imported
import cv2
# Create a Video Reader Object.
cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print("Error in opening video stream or file")
#Define the codec for the Video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#Create Video Writer Object
writer = cv2.VideoWriter('output.avi',fourcc, 20.0, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        writer.write(frame)
        cv2.imshow("Frame",frame)
        # Exit on pressing esc
        if cv2.waitKey(20) & 0xFF == 27:
            break
    else:
        break
cap.release()
writer.release()
cv2.destroyAllWindows()
'''
#add, blend
import cv2
import numpy as np

a = cv2.imread('6pack_resized.jpg')
b = cv2.imread('6pack_cut_resized.jpg')
c = cv2.add(a,b)
d = cv2.addWeighted(a,0.4,b,0.4,0)

while(1):
    cv2.imshow('c',c)
    cv2.imshow('d',d)
    k = cv2.waitKey(0) & 0xff
    if k == 27:
        break

cv2.destroyAllWindows()