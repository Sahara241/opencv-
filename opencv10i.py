#How to Bind Trackbar to Opencv Windows
import numpy as np
import cv2 as cv

def func(x):
    print(x)

cv.namedWindow('image')

cv.createTrackbar('n','image',50,500,func)


switch='color/gray'
cv.createTrackbar(switch,'image',0,1,func)

while(1):
    img=cv.imread('lena.jpg')
    pos=cv.getTrackbarPos('n','image')
    font=cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img,str(pos),(50,150),font,4,(0,255,0))
    
    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    
    s=cv.getTrackbarPos(switch,'image')

    if s == 0:
        pass 
    else:
        img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    
    img=cv.imshow('image',img)

cv.destroyAllWindows()