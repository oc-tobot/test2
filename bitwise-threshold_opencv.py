#testing of bitwise operation and image blending

import cv2
#step1: load the image
img1 = cv2.imread('6pack_cut.jpg')
img2 = cv2.imread('6pack_cut_resized.jpg')
e1 = cv2.getTickCount()
#step2: creat a region of interest on where you want
rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

#step3: creat the binary image (just 0 and 1, black and white)
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
ret, mask = cv2.threshold(img2gray, 254, 255, cv2.THRESH_BINARY) #loc bo phan mau trang (>254), trong vi du la loc bo phan mau den (<10), nen minh phai dao vi tri cua mask va maskinv trong step 4 va 5
maskinv = cv2.bitwise_not(mask)

#step4: 
img1_bg = cv2.bitwise_and(roi,roi,mask = mask)
#step5:
img2_fg = cv2.bitwise_and(img2,img2,mask =maskinv)
#step6:
dst = cv2.add(img1_bg,img2_fg)
img1[0:rows, 0:cols] = dst

cv2.imshow('step1', img2)
cv2.imshow('anh1.jpg',mask)
cv2.imshow('anh2.jpg', maskinv)
cv2.imshow('anh3.jpg', img1_bg)
cv2.imshow('anh4.jpg', img2_fg)
cv2.imshow('anh5.jpg', dst)
cv2.imshow('anh6.jpg', img1)

e2 = cv2.getTickCount()
time = (e2-e1)/cv2.getTickFrequency()
print(time)
cv2.waitKey(0)
cv2.destroyAllWindows()
