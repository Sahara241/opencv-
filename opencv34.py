# Detect Corners with Harris Corner Detector in OpenCV
import numpy as np
import cv2

img=cv2.imread('edge.jpg')

cv2.imshow('image',img)
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

gray=np.float32(gray)
dst=cv2.cornerHarris(gray,2,3,0.04) #we can also put k=0.06
dst=cv2.dilate(dst,None)

img[dst > 0.01 * dst.max()]=[255,0,0]
cv2.imshow('dst',img)
if cv2.waitKey(0) & 0xFF==27:
    cv2.destroyAllWindows()
