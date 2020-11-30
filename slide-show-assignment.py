#assignment :creat a slide show of images in a folder using cv2.addweighted
import cv2
import numpy as np
img0 = cv2.imread('6pack_cut_resized.jpg')
img1 = cv2.imread('anh1.jpg')
img2 = cv2.imread('anh2.jpg')
img3 = cv2.imread('anh3.jpg')
img4 = cv2.imread('anh4.jpg')
img5 = cv2.imread('anh5.jpg')
img6 = cv2.imread('anh6.jpg')
list_img = [img0,img1,img2,img3,img4,img5,img6]


while(1):
    for i in range(6):
        cv2.imshow('slide', list_img[i])
        k = cv2.waitKey(0) & 0xff
        if k == ord(" "):
            for j in range(50):
                temp = cv2.addWeighted(list_img[i+1],j/50, list_img[i],(50-j)/50,0)
                cv2.imshow('slide',temp)
                #the code below wont worl out like it should be. i dont know why
                if k == ord("c"):
                    cv2.imshow('slide', list_img[i+1])
                cv2.waitKey(20)
    break


cv2.destroyAllWindows()