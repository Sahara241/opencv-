#How to Bind Trackbar to Opencv Windows
import numpy as np
import cv2 as cv

def func(x):
    print(x)

img=np.zeros((300,512,3),np.uint8)
cv.namedWindow('image')

cv.createTrackbar('B','image',0,255,func)
cv.createTrackbar('G','image',0,255,func)
cv.createTrackbar('R','image',0,255,func)

switch='0 : OFF\n 1 : ON'
cv.createTrackbar(switch,'image',0,1,func)

while(1):
    cv.imshow('image',img)
    k=cv.waitKey(1) & 0xFF
    if k==27:
        break
    
    b=cv.getTrackbarPos('B','image')
    g=cv.getTrackbarPos('G','image')
    r=cv.getTrackbarPos('R','image')
    s=cv.getTrackbarPos(switch,'image')

    if s == 0:
        img[:]=0
    else:
        img[:]=[b,g,r]

cv.destroyAllWindows()