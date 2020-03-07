#Detect corner with Shi Tomashi corner detector in opencv
# for image
import cv2
import numpy as np

img=cv2.imread('blox.jpg')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

corners=cv2.goodFeaturesToTrack(gray,100,0.01,10)

corners=np.int0(corners) #alias of int64(int64==int0) 

for i in corners:
    x,y=i.ravel()
    cv2.circle(img,(x,y),4,255,-1)

cv2.imshow('dst',img)
if cv2.waitKey(0) & 0XFF==ord('q'):
    cv2.destroyAllWindows()


Detect corner with Shi Tomashi corner detector in opencv

#for video
#import cv2 as cv
#import numpy as np
#
#cap=cv.VideoCapture(0)
#
#while (cap.isOpened()):
#    ret,frame=cap.read()
#    
#    if ret==False:
#        break
#
#    gray=cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
#    corners=cv.goodFeaturesToTrack(gray,10,0.01,10)
#    corners=np.int0(corners) #alias of int64(int64==int0) 
#
#
#    for i in corners:
#        x,y=i.ravel()
#        cv.circle(frame,(x,y),3,255,-1)
#    
#    cv.imshow('frame',frame)
#
#    keyword=cv.waitKey(30)
#    if keyword==ord('q') or keyword==27:
#        break
#
#
#cap.release()
#cv.destroyAllWindows()