from cv2 import cv2  
import numpy as np
#doc anh    flag = 0 thi load anh den trang, flag = 1 thi load anh mau
img = cv2.imread('6pack_cat.jpg', 1)

##show anh ra ma hinh
cv2.imshow('image', img)                

#dong code nay de giu buc anh lai tren man hinh cho den khi thoat
cv2.waitKey(0)                              

#giai phong bo nho
cv2.destroyAllWindows()
