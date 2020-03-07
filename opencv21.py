#Find and Draw Contours with OpenCV in Python
import cv2
import numpy as np

img=cv2.imread('opencv-logo.png')
imgray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh=cv2.threshold(imgray,127,255,0)
contours,hierarchy=cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
print("Number of contours:"+str(len(contours)))
print(contours[0])

cv2.drawContours(img,contours,-1,(0,255,0),3) # -1 for all 9 contours in image

cv2.imshow('image',img)
cv2.imshow('Image Gray',imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()