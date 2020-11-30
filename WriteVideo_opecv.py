#capture and write down the video in real time into ouput.avi, avi can be replace by mp4 ,...
#drawing rectangle in video in real time (not on mouse click)
#Import only if not previously imported
import cv2
# Create a Video Reader Object.
cap = cv2.VideoCapture(0)
if cap.isOpened() == False:
    print("Error in opening video stream or file")
#Define the codec for the Video
fourcc = cv2.VideoWriter_fourcc(*"XVID")
#Create Video Writer Object
writer = cv2.VideoWriter('output.avi',fourcc, 13, (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))))
font = cv2.FONT_HERSHEY_SIMPLEX
ret, frame = cap.read()
while (cap.isOpened()):
    ret, frame = cap.read()
    frame = cv2.flip(frame ,1)
    cv2.rectangle(frame, (200,150), (300,300), (255,255,0), 2)
    cv2.rectangle(frame, (400,50), (500,210), (255,255,0), 2)
    cv2.putText(frame,'recognized face',(0,30),font,1,(255,255,255),1)
    writer.write(frame)
    cv2.imshow('Frame',frame)
    # Exit on pressing esc
    if cv2.waitKey(50) & 0xFF == 27:
        break
cap.release()
writer.release()
cv2.destroyAllWindows()