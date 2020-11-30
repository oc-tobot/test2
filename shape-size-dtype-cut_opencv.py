from cv2 import cv2
import numpy as mp

img = cv2.imread("6pack_cat.jpg", 1)
#chieu cao, chieu rong, loai hinh anh(rgb hay den trang)
print('height = ', img.shape[0], '; wigth = ',img.shape[1] ) 
#kich co buc anh(so pixel = chieu cao nhan chieu rong)
print(img.size)
#loai cua buc anh(uint8: unsigned int 8bit or 8byte)
print(img.dtype)
#cat anh
subimg = img[200:550,420:870]
cv2.imshow('anh da cat', subimg)
cv2.waitKey(0)

cv2.destroyAllWindows()