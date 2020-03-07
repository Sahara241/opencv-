#Handle Mouse Events in OpenCV
import cv2
import numpy as np

#events=[i for i in dir(cv2) if 'EVENT' in i]
#print(events)

def click_event(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,', ',y)
        strXY=str(x)+', '+ str(y) 
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,strXY,(x,y),font,.4,(255,255,0),2,cv2.LINE_AA)
        cv2.imshow('image',img)
    if event == cv2.EVENT_RBUTTONDOWN:
        blue=img[y,x,0]
        green=img[y,x,1]
        red=img[y,x,2]
        strBGR=str(blue) + ', ' + str(green) + ', '+str(red)
        font=cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(img,strBGR,(x,y),font,.4,(0,0,255),2,cv2.LINE_AA)
        cv2.imshow('image',img)

#img=np.zeros((512,512,3),np.uint8)
img=cv2.imread('lena.jpg')
cv2.imshow('image',img)

cv2.setMouseCallback('image',click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
