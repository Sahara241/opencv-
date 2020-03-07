# How to Use Background Subtraction Methods in OpenCV
import numpy as np
import cv2

cap = cv2.VideoCapture('vtest.avi')
#fgbg = cv2.bgsegm.createBackgroundSubtractorMOG()
#fgbg = cv2.createBackgroundSubtractorMOG2()
#fgbg = cv2.createBackgroundSubtractorMOG2(detectShadows=False)
#kernel=cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
#fgbg = cv2.bgsegm.createBackgroundSubtractorGMG()
fgbg = cv2.createBackgroundSubtractorKNN(detectShadows=False)
while (cap.isOpened()):
    ret,frame=cap.read()

    if ret==False:
        break
    fgmask=fgbg.apply(frame)
    #fgmask=cv2.morphologyEx(fgmask,cv2.MORPH_OPEN,kernel)

    cv2.imshow('frame',frame)
    cv2.imshow('FG MASK frame',fgmask)
    
    keyword=cv2.waitKey(30)
    if keyword==ord('q') or keyword==27:
        break
cap.release()        
cv2.destroyAllWindows()
